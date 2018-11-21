import socket
import time

def get_circuit_frequency():
    circuit_frequency = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8291

    s.connect((host, port))
    dados = s.recv(1024)
    print(dados.decode('ascii'))


def set_circuit_frequency():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""  #127.0.0.1
    port = 8291

    msg = "Hello World!"

    s.bind((host, port))
    s.listen(1)

    while True:
        time.sleep(5)
        c, e = s.accept()
        print("Conectado com ", e)
        c.send(msg.encode('ascii'))
        c.close()


set_circuit_frequency()
