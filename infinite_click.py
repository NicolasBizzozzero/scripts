import pyautogui
import time


COORDINATE = (15, 15)
SLEEPING_TIME = 0.5


def main():
    try:
        while True:
            time.sleep(SLEEPING_TIME)
            pyautogui.click(*COORDINATE)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
