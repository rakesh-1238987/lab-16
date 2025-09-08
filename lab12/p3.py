import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sine_5 = np.sin(2 * np.pi * 5 * t)
sine_5_shifted = np.sin(2 * np.pi * 5 * (t - 0.1))

plt.figure(figsize=(8, 4))
plt.plot(t, sine_5, label="Original")
plt.plot(t, sine_5_shifted, label="Shifted (0.1s)")
plt.title("c) 5 Hz Sine Wave (Time Shifted)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
