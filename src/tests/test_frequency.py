import pytest
import wave
import pyaudio
import numpy as np
from detect_tone import comput_frequency


def get_sound_data(file):
    a_note = wave.wf = wave.open(file, 'rb')
    CHUNK = 2048 
    audio = pyaudio.PyAudio()
    stream = audio.open(format = pyaudio.paInt16,
                channels = a_note.getnchannels(),
                rate = a_note.getframerate(),
                output = True)

    data = np.frombuffer(a_note.readframes(CHUNK), np.int16)   
    return data    

def test_comput_frequency():

    # Geting Data from wav files
    data_440 = get_sound_data('tests/sound_sample/440hz.wav')

    data_82 = get_sound_data('tests/sound_sample/82.4hz.wav')
    data_110 = get_sound_data('tests/sound_sample/110hz.wav')
    data_146 = get_sound_data('tests/sound_sample/146.8hz.wav')
    data_196 = get_sound_data('tests/sound_sample/196hz.wav')
    data_246 = get_sound_data('tests/sound_sample/246.9hz.wav')
    data_329 = get_sound_data('tests/sound_sample/329.6hz.wav')

    # Computing frequencys
    frequency_440 = comput_frequency(data_440)

    frequency_82 = comput_frequency(data_82)    
    frequency_110 = comput_frequency(data_110)
    frequency_146 = comput_frequency(data_146)
    frequency_196 = comput_frequency(data_196)
    frequency_246 = comput_frequency(data_246)
    frequency_329 = comput_frequency(data_329)


    assert (frequency_440 > 429 and frequency_440 < 431)
    
    
    assert (frequency_82 > 81 and frequency_82 < 83)
    assert (frequency_110 > 109 and frequency_110 < 111)
    assert (frequency_146 > 145 and frequency_146 < 147)
    assert (frequency_196 > 195 and frequency_196 < 197)
    assert (frequency_246 > 245 and frequency_246 < 247)
    assert (frequency_329 > 328 and frequency_329 < 330)
    




