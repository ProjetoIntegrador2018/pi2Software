import os
import pytest
import wave
import pyaudio
import numpy as np
from src.detect_tone import comput_frequency


def get_sound_data(file):
    a_note = wave.wf = wave.open(file, 'rb')
    CHUNK = 2048

    #data = np.frombuffer(a_note.readframes(CHUNK), np.int16)
    
    data = a_note.readframes(CHUNK)
    
    return data


def test_comput_frequency():
    # Geting Data from wav files

    data_82 = get_sound_data('src/tests/sound_sample/82.4hz.wav')
    data_110 = get_sound_data('src/tests/sound_sample/110hz.wav')
    data_146 = get_sound_data('src/tests/sound_sample/146.8hz.wav')
    data_196 = get_sound_data('src/tests/sound_sample/196hz.wav')
    data_246 = get_sound_data('src/tests/sound_sample/246.9hz.wav')
    data_329 = get_sound_data('src/tests/sound_sample/329.6hz.wav')

    # Computing frequencys

    frequency_82 = comput_frequency(data_82)  *2
    frequency_110 = comput_frequency(data_110)*2
    frequency_146 = comput_frequency(data_146)*2
    frequency_196 = comput_frequency(data_196)*2
    frequency_246 = comput_frequency(data_246)*2
    frequency_329 = comput_frequency(data_329)*2

    assert (frequency_82 > 80.6 and frequency_82 < 83.4)
    assert (frequency_110 > 109 and frequency_110 < 111)
    assert (frequency_146 > 145 and frequency_146 < 147)
    assert (frequency_196 > 195 and frequency_196 < 197)
    assert (frequency_246 > 245 and frequency_246 < 247)
    assert (frequency_329 > 328 and frequency_329 < 330)
