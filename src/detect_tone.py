import pyaudio
import numpy as np
import time
import store
import socket

from math import log2, pow


delta82 = -4
delta110 = 3
delta146 = -4
delta196 = 3
delta246 = 10
delta329 = 7


def comput_frequency(audio_data):
    frate = 44100.0
    w = np.fft.fft(audio_data)
    freqs = np.fft.fftfreq(len(w))
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    frequency = abs(freq * frate)

    if(frequency > 85 and frequency < 87):
        return frequency + delta82

    if(frequency > 106 and frequency < 108):
        return frequency + delta110

    if(frequency > 149 and frequency < 151):
        return frequency + delta146

    if(frequency > 192 and frequency < 194):
        return frequency + delta196

    if(frequency > 235 and frequency < 237):
        return frequency + delta246

    if(frequency > 321 and frequency < 323):
        return frequency + delta329

    return frequency


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
        c, e = s.accept()
        print("Conectado com ", e)
        c.send(msg.encode('ascii'))
        c.close()


def compare_frequency(frequency, circuit_frequency):
    frequency_error_range = 10

    if abs(frequency - circuit_frequency) >= frequency_error_range:
        print("frequency error range")
        return frequency
    else:
        print("actual frequency")
        return (frequency + circuit_frequency)/2


def get_tone():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 2048
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    stream.start_stream()

    while(1):
        audio_data = np.fromstring(stream.read(CHUNK), np.int16)
        frequency = comput_frequency(audio_data)
        # circuit_frequency = get_circuit_frequency()

        # mean_frequency = compare_frequency(frequency, circuit_frequency)

        if(frequency > 0):
            store.frequency = frequency

    stream.stop_stream()
    stream.close()

    audio.terminate()
