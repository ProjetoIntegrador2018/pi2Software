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


def fetch_frequency(frequency):
    host = '169.254.115.63'
    port = 8291

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    msg = s.recv(1024)
    msg = msg.decode()
    result = compare_frequency(frequency, msg)
    result = str(result).encode()

    if result:
        s.send(result)


def compare_frequency(frequency, circuit_frequency):
    frequency_error_range = 10
    circuit_frequency = float(circuit_frequency)	
  
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
        audio_data = np.fromstring(stream.read(CHUNK, exception_on_overflow=False), np.int16)
        frequency = comput_frequency(audio_data)
        
        fetch_frequency(frequency)

        if(frequency > 0):
            store.frequency = frequency

    stream.stop_stream()
    stream.close()

    audio.terminate()
