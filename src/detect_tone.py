import pyaudio
import numpy as np
import time
from math import log2, pow
import store

        
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

        aux = []
        time_aux = 0

        while(1):
                audio_data = np.fromstring(stream.read(CHUNK), np.int16)
                frate = 44100.0
                w = np.fft.fft(audio_data)
                freqs = np.fft.fftfreq(len(w))
                idx = np.argmax(np.abs(w))
                freq = freqs[idx]
                frequency = abs(freq * frate)
                if(frequency > 0):
                        store.frequency = frequency   

        stream.stop_stream()
        stream.close()

        audio.terminate()
