import pyaudio
import numpy as np
import time
import store
import socket


delta82 = -4
delta110 = 3
delta146 = -4
delta196 = 3
delta246 = 10
delta329 = 7

host = '169.254.72.67'
port = 8291
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except ConnectionRefusedError:
    print("Connection Refused Error! get_circuit_frequency")
except Exception:
    print("")

def fetch_frequency(frequency):
    try:
        msg = s.recv(1024)
        msg = msg.decode()
        #print(msg)
        result = frequency
        # result = 10
        result = str(result).encode()
        if result:
            s.send(result)
    except  Exception:
        #print("Error connection socket!")
        pass

def compare_frequency(frequency, circuit_frequency):
    frequency_error_range = 10
    circuit_frequency = float(circuit_frequency)

    if abs(frequency - circuit_frequency) >= frequency_error_range:
        #print("frequency error range")
        return frequency
    else:
        #print("actual frequency")
        return (frequency + circuit_frequency)/2


def get_tone():

    NOTE_MIN = -20
    NOTE_MAX = 400
    FSAMP = 22050       # Sampling frequency in Hz
    FRAME_SIZE = 2048   # How many samples per frame?
    FRAMES_PER_FFT = 32 # FFT takes average across how many frames?

    SAMPLES_PER_FFT = FRAME_SIZE*FRAMES_PER_FFT
    FREQ_STEP = float(FSAMP)/SAMPLES_PER_FFT


    NOTE_NAMES = 'C C# D D# E F F# G G# A A# B'.split()

    def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
    def number_to_freq(n): return 440 * 2.0**((n-69)/12.0)
    def note_name(n): return NOTE_NAMES[n % 12] + str(n/12 - 1)


    # Get min/max index within FFT of notes we care about.
    # See docs for numpy.rfftfreq()
    def note_to_fftbin(n): return number_to_freq(n)/FREQ_STEP
    imin = max(0, int(np.floor(note_to_fftbin(NOTE_MIN-1))))
    imax = min(SAMPLES_PER_FFT, int(np.ceil(note_to_fftbin(NOTE_MAX+1))))

    # Allocate space to run an FFT.
    buf = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
    num_frames = 0

    stream = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=FSAMP,
                                    input=True,
                                    frames_per_buffer=FRAME_SIZE)

    stream.start_stream()

    # Create Hanning window function
    window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, SAMPLES_PER_FFT, False)))

    print ('sampling at' +str(FSAMP)+ 'Hz with max resolution of'+ str(FREQ_STEP)+ 'Hz')

    while stream.is_active():

        # Shift the buffer down and new data in
        buf[:-FRAME_SIZE] = buf[FRAME_SIZE:]
        buf[-FRAME_SIZE:] = np.fromstring(stream.read(FRAME_SIZE, exception_on_overflow=False), np.int16)

        # Run the FFT on the windowed buffer
        fft = np.fft.rfft(buf * window)

        # Get frequency of maximum response in range
        freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP

        # Get note number and nearest note
        n = freq_to_number(freq)
        n0 = int(round(n))

        num_frames += 1

        if num_frames >= FRAMES_PER_FFT:
            fetch_frequency(freq)
            store.frequency = freq
