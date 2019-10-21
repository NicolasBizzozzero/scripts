""" Check who is not following you back on Instagram.

Source :
https://github.com/tuxity/insta-unfollower
"""

import time
import requests
import json
import re

from getpass import getpass


TIME_SLEEPING = 1000

URL_INSTAGRAM = 'https://www.instagram.com'
URL_INSTAGRAM_LOGIN = '%s/accounts/login/ajax/' % URL_INSTAGRAM
URL_INSTAGRAM_LOGOUT = '%s/accounts/logout/' % URL_INSTAGRAM
URL_INSTAGRAM_PROFILE = '%s/%s/'
URL_INSTAGRAM_QUERY = '%s/graphql/query/' % URL_INSTAGRAM
URL_INSTAGRAM_UNFOLLOW = '%s/web/friendships/%s/unfollow/'


def main(instagram_username, instagram_password, ignore_verified=False,
         unfollow=False):
    session = login(instagram_username, instagram_password)
    user_info = get_user_info(session, instagram_username)
    print('Successfully connected as {} ({} followers, {} following)'.format(
        user_info['username'],
        user_info['edge_followed_by']['count'],
        user_info['edge_follow']['count'])
    )

    followers_list = get_followers_list(session)
    following_list = get_following_list(session)

    bitches_not_following = \
        [user for user in following_list if user not in followers_list]
    print('You are following {} user(s) who are not following you.'.format(
        len(bitches_not_following)))

    if len(bitches_not_following) > 0:
        for user in bitches_not_following:
            if ignore_verified and user['is_verified']:
                continue

            print("User ", user['username'],
                  " (VERIFIED)" if user['is_verified'] else "",
                  " is not following you back.", sep="")

            if unfollow:
                unfollow_that_bitch(session, bitch_to_unfollow=user)
    logout(session)


def login(instagram_username, instagram_password):
    global URL_INSTAGRAM, URL_INSTAGRAM_LOGIN

    session = requests.Session()
    session.headers.update({
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.instagram.com',
        'Origin': 'https://www.instagram.com',
        'Referer': 'https://www.instagram.com/',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'),
        'X-Instagram-AJAX': '1',
        'X-Requested-With': 'XMLHttpRequest'
    })
    session.cookies.update({
        'ig_pr': '1',
        'ig_vw': '1920',
    })

    reponse = session.get(URL_INSTAGRAM)
    session.headers.update({
        'X-CSRFToken': re.search(r'(?<=\"csrf_token\":\")\w+',
                                 reponse.text).group(0)
    })

    credentials = {
        'username': instagram_username,
        'password': instagram_password
    }

    response = session.post(URL_INSTAGRAM_LOGIN, data=credentials,
                            allow_redirects=True)

    if json.loads(response.text)['authenticated']:
        session.headers.update({
            'X-CSRFToken': response.cookies['csrftoken']
        })
    else:
        print("Cannot login with the given credentials")
        exit(1)
    return session


def get_user_info(session, instagram_username):
    global URL_INSTAGRAM_PROFILE, URL_INSTAGRAM

    response = session.get(URL_INSTAGRAM_PROFILE %
                           (URL_INSTAGRAM, instagram_username))
    extract = re.search(r'window._sharedData = (.+);</script>',
                        str(response.text))
    response = json.loads(extract.group(1))
    return response['entry_data']['ProfilePage'][0]['graphql']['user']


def get_followers_list(session):
    global URL_INSTAGRAM_QUERY

    # Querying followers
    query_hash = '56066f031e6239f35a904ac20c9f37d9'
    variables = {
        "id": session.cookies['ds_user_id'],
        "include_reel": False,
        "fetch_mutual": False,
        "first": 50
    }
    response = _query_until_response(session, url=URL_INSTAGRAM_QUERY,
                                     params={
                                         'query_hash': query_hash,
                                         'variables': json.dumps(variables)
                                     })
    response = json.loads(response.text)

    # Computing list of followers with the user's followers graph
    followers_list = []
    for edge in response['data']['user']['edge_followed_by']['edges']:
        followers_list.append(edge['node'])

    while response['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        variables['after'] = response['data']['user']['edge_followed_by']['page_info']['end_cursor']
        response = _query_until_response(session, url=URL_INSTAGRAM_QUERY,
                                         params={
                                             'query_hash': query_hash,
                                             'variables': json.dumps(variables)
                                         })
        response = json.loads(response.text)

        for edge in response['data']['user']['edge_followed_by']['edges']:
            followers_list.append(edge['node'])

    return followers_list


def get_following_list(session):
    global URL_INSTAGRAM_QUERY

    # Querying following
    query_hash = 'c56ee0ae1f89cdbd1c89e2bc6b8f3d18'
    variables = {
        "id": session.cookies['ds_user_id'],
        "include_reel": False,
        "fetch_mutual": False,
        "first": 50
    }
    response = _query_until_response(session, url=URL_INSTAGRAM_QUERY,
                                     params={
                                         'query_hash': query_hash,
                                         'variables': json.dumps(variables)
                                     })
    response = json.loads(response.text)

    # Computing list of following with the user's following graph
    follows_list = []
    for edge in response['data']['user']['edge_follow']['edges']:
        follows_list.append(edge['node'])

    while response['data']['user']['edge_follow']['page_info']['has_next_page']:
        variables['after'] = response['data']['user']['edge_follow']['page_info']['end_cursor']
        response = _query_until_response(session, url=URL_INSTAGRAM_QUERY,
                                         params={
                                             'query_hash': query_hash,
                                             'variables': json.dumps(variables)
                                         })
        response = json.loads(response.text)

        for edge in response['data']['user']['edge_follow']['edges']:
            follows_list.append(edge['node'])

    return follows_list


def unfollow_that_bitch(session, bitch_to_unfollow):
    global URL_INSTAGRAM, URL_INSTAGRAM_PROFILE

    response = session.get(URL_INSTAGRAM_PROFILE %
                           (URL_INSTAGRAM, bitch_to_unfollow['username']))

    # update header again, idk why it changed
    session.headers.update({
        'X-CSRFToken': response.cookies['csrftoken']
    })

    response = session.get(URL_INSTAGRAM_UNFOLLOW %
                           (URL_INSTAGRAM, bitch_to_unfollow['id']))
    while response.status_code != 200:
        # querying too much, sleeping a bit before querying again
        time.sleep(TIME_SLEEPING)
        response = session.get(URL_INSTAGRAM_UNFOLLOW %
                               (URL_INSTAGRAM, bitch_to_unfollow['id']))


def logout(session):
    global URL_INSTAGRAM_LOGOUT

    post_data = {
        'csrfmiddlewaretoken': session.cookies['csrftoken']
    }

    logout = session.post(URL_INSTAGRAM_LOGOUT, data=post_data)

    return logout.status_code == 200


def _query_until_response(session, url, params={},
                          time_sleeping=TIME_SLEEPING):
    response = session.get(url, params=params)
    while response.status_code != 200:
        # querying too much, sleeping a bit before querying again
        time.sleep(TIME_SLEEPING)
        response = session.get(url, params=params)
    return response


if __name__ == "__main__":
    instagram_username = input("Enter your Instagram username: ").strip()
    instagram_password = getpass("Enter your Instagram password: ").strip()
    main(instagram_username, instagram_password, ignore_verified=False,
         unfollow=False)
