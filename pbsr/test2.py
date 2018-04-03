import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import _thread
import time

def easy_sound(freq, pos):
    fbins = [1.570, 4.714, 7.862, 11.0186, 14.18624, 33.616, 36.7912, 40.3274, 43.744];

    stream = sd.OutputStream(dtype = np.int16, channels=2)
    stream.start()
    time = 2.0
    wave = 0;
    samples = np.arange(44100*1*time)/44100.0
    for i in range(len(fbins)):
        if (fbins[i]*freq > 20000.0):
            break;
        a = np.sin(np.pi*(i+1)*pos/1.0)/(343*fbins[i]*freq)
        alpha = (1/4)*1*(2-(np.sin(2*np.pi*(i+1))/(np.pi * (i+1))))
        a /= alpha
        print(a)
        wave += a * np.sin(2*np.pi*(fbins[i]*freq)*samples)

    wave *= 100000000

    for i in range(len(wave)):
        # print(wave[i])
        wave[i] *= np.exp(-2.0*(i/44100))

    wav_wave = np.array(wave, dtype=np.int16)
    stream.write(wav_wave)
    stream.close()
    scipy.io.wavfile.write('out.wav', 44100, wav_wave)
    return wav_wave





def mario():
    _thread.start_new_thread(easy_sound, (261, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (277, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (293, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (311, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (329, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (349, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (369, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (391, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (415, 0.2))
    time.sleep(0.2)
    _thread.start_new_thread(easy_sound, (440, 0.2))

