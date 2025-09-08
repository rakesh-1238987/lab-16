import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sine_10 = np.sin(2 * np.pi * 10 * t)
sine_10_scaled = 3 * sine_10

plt.figure(figsize=(8, 4))
plt.plot(t, sine_10, label="Original")
plt.plot(t, sine_10_scaled, label="Scaled (x3)")
plt.title("d) 10 Hz Sine Wave (Amplitude Scaled)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
