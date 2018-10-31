from screens import Application
from detect_tone import get_tone
from threading import Thread
from kivy.config import Config


Config.read("config.ini")


def run_frontend():
    Application().run()


if __name__ == "__main__":
    thread1 = Thread(target=run_frontend)
    thread2 = Thread(target=get_tone)
    thread1.start()
    thread2.start()
