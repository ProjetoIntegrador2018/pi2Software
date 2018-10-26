import pyaudio
import numpy as np
import time
from math import log2, pow
import store

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
                frequency = comput_frequency(audio_data)
                if(frequency > 0):
                        store.frequency = frequency   

        stream.stop_stream()
        stream.close()

        audio.terminate()
