import sounddevice as sd
import numpy as np

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
        wave[i] *= np.exp(-3.0*(i/44100))

    wav_wave = np.array(wave, dtype=np.int16)
    stream.write(wav_wave)
    stream.close()
    return wav_wave




