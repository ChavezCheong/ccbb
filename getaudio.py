import sounddevice as sd
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from scipy.fftpack import fft
from scipy import signal
from scipy.signal import argrelextrema, fftconvolve


#set defaults
sd.default.samplerate = 44100
sd.default.channels = 2

# time.sleep(5) #This is the fastest way of doing it, but some people prefer more dynamic methods. Can google.


duration = 4 #seconds
myrecording = sd.rec(int(duration * 44100), blocking = True)

signal = myrecording

freqs = fft(signal)

#Plot both the wave and its spectrum
fig = plt.figure(figsize=(8, 6))
gs1 = gridspec.GridSpec(2, 1, height_ratios=[1, 1]) 
ax1, ax2 = fig.add_subplot(gs1[0]), fig.add_subplot(gs1[1])

ax1.plot(signal, color="#6480e5")
ax2.plot(np.abs(freqs), color="#6480e5")

ax1.set_title('Signal Wave'), ax2.set_title("Frequency Plot")
ax1.set_xlim([0, 1e5]), ax2.set_xlim([0, 5e3])
ax1.set_ylim([-4e4, 4e4]), ax2.set_ylim([0, 1.5e8])
ax1.set_xlabel('Sampling Points'), ax2.set_xlabel('Frequency (Hz)')
ax1.set_ylabel('Amplitude'), ax2.set_ylabel('Intensity') 
ax1.ticklabel_format(style='sci', axis='both', scilimits=(0,0)) 
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.tight_layout()
