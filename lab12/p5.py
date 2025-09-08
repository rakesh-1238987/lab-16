import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)

sine_5 = np.sin(2 * np.pi * 5 * t)
sine_5_reversed = sine_5[::-1]

plt.figure(figsize=(8, 4))
plt.plot(t, sine_5, label="Original")
plt.plot(t, sine_5_reversed, label="Reversed")
plt.title("e) 5 Hz Sine Wave (Time Reversal)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
