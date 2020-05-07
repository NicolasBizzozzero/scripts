import subprocess



def main():
    channel = "lofi"
    if channel == "lofi":
        url = r"https://www.youtube.com/watch?v=5qap5aO4i9A"

    url = subprocess.run(["youtube-dl", "-g", url], stdout=subprocess.PIPE)
    print(url.stdout.decode("utf8"))


if __name__ == "__main__":
    main()

