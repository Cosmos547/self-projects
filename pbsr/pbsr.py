import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import _thread
import time
from exp import *

def easy_sound(freq, pos, decay, fbins):

    stream = sd.OutputStream(dtype = np.int16, channels=2)
    stream.start()
    time = 0.4
    wave = 0;
    samples = np.arange(44100*1*time)/44100.0
    count = 0
    for i in range(len(fbins)):
        if (fbins[i]*freq > 20000.0):
            break
        count += 1
        cf = fbins[i]*freq
        idf = 0.005
        a = np.sin(np.pi*(i+1)*pos/1.0)/(343*fbins[i]*freq)
        alpha = (1/4)*1*(2-(np.sin(2*np.pi*(i+1))/(np.pi * (i+1))))
        a /= alpha
        print(str(i) + " " + str(a))
        wave += a * np.exp(-decay*cf*idf*samples) * np.sin(2*np.pi*(fbins[i]*freq)*samples)

    count = 1/count
    wave *= count

    # for i in range(len(wave)):
        # print(wave[i])
        # wave[i] *= np.exp(-decay*(i/44100))

    wav_wave = np.array(wave/np.max(np.abs(wave))*32767, dtype=np.int16)
    stream.write(wav_wave)
    stream.close()
    # scipy.io.wavfile.write(str(freq) + '.wav', 44100, wav_wave)
    return wav_wave



# nodes = [5, 15, 50, 150, 1000, 1500]

# fbins = []

# for i in nodes:
    # fbins.append(bar(i))

# for i in fbins:
    # _thread.start_new_thread(easy_sound, (260, 0.5, 1, i))
    # time.sleep(3.0)

# fbin0 = bar(1000)

# for i in range(1,10):
    # i = 0.1*i
    # _thread.start_new_thread(easy_sound, (440, i, 1, fbin0))
    # easy_sound(440, i, 5, fbin0)

# freqs = [261, 277, 293, 311, 329, 349, 369, 391, 415, 440]

# for i in freqs:
    # easy_sound(i, 0.5, 3, fbin0)
