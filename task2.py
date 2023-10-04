import numpy as np
import matplotlib.pyplot as plt

# Time values
t = np.linspace(0, 1, 1000, endpoint=False)  # 1000 points from 0 to 1 second

# Signal 𝑓(𝑡) = sin(𝑡)
f_t = np.sin(2 * np.pi * t)

# Calculate the FFT of the signal
fft_result = np.fft.fft(f_t)

# Calculate the corresponding frequencies for the FFT result
frequencies = np.fft.fftfreq(len(fft_result), 1 / len(t))

# Plot the magnitude of the frequency spectrum
plt.figure(figsize=(20, 10))
plt.stem(frequencies, np.abs(fft_result), markerfmt='ro', basefmt=" ", linefmt="r-", use_line_collection=True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum of 𝑓(𝑡) = sin(𝑡)')
plt.grid(True)
plt.show()

t_square = np.linspace(0, 1, 1000, endpoint=False)  # 1000 points from 0 to 1 second

# Signal 𝑔(𝑡)
g_t = np.zeros_like(t_square)

# Define the square wave signal g(t) in the given time intervals
g_t[(0 <= t_square) & (t_square < 0.5)] = 1
g_t[(0.5 <= t_square) & (t_square < 1)] = 0

# Calculate the FFT of the square wave signal
fft_result_square = np.fft.fft(g_t)

# Calculate the corresponding frequencies for the FFT result
frequencies_square = np.fft.fftfreq(len(fft_result_square), 1 / len(t_square))

# Plot the magnitude of the frequency spectrum for the square wave
plt.figure(figsize=(8, 4))
plt.stem(frequencies_square, np.abs(fft_result_square), markerfmt='go', basefmt=" ", linefmt="g-", use_line_collection=True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum of 𝑔(𝑡) (Square Wave)')
plt.grid(True)
plt.show()