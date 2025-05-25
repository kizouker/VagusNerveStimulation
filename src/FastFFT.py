import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

signal = np.sin(2*np.pi*8*np.linspace(0,1,500))  # 8 Hz signal
spectrum = np.abs(fft(signal))
plt.plot(spectrum)
plt.show()
