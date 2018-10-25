from telas import Aplicacao
from detect_tone import get_tone
from threading import Thread


def run_frontend():
    Aplicacao().run()


if __name__ == "__main__":

    thread1 = Thread( target=run_frontend)
    thread2 = Thread( target=get_tone)
    thread1.start()    
    thread2.start()

    
