import numpy as np
import matplotlib.pyplot as plt

# Define an 8-bit binary sequence
bit_sequence = [1, 0, 1, 0, 1, 0, 1, 0]

# Bit rate in bits per second
bit_rate = 3  # 1 bit/sec

# Time duration for each bit
bit_duration = 1 / bit_rate  # 1 second/bit

# Time values for the signal
time = np.arange(0, len(bit_sequence) * bit_duration, bit_duration)

# Create the line code (assign +5V to bit 1 and 0V to bit 0)
line_code = [5 if bit == 1 else 0 for bit in bit_sequence]

# Plot the time vs. amplitude of the line code
plt.figure(figsize=(10, 4))
plt.step(time, line_code, where='post', color='b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Line Code (8-bit frame, 1 bit/sec)')
plt.grid(True)
plt.show()

# Calculate the magnitude of the frequency response using FFT
fft_result = np.fft.fft(line_code)
frequencies = np.fft.fftfreq(len(fft_result))

# Plot the magnitude of the frequency response
plt.figure(figsize=(10, 4))
plt.stem(frequencies, np.abs(fft_result), markerfmt='ro', basefmt=" ", linefmt="r-", use_line_collection=True)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response (8-bit frame, 1 bit/sec)')
plt.grid(True)
plt.show()

# Suppress frequency components above the 5th harmonic, including the fundamental frequency
harmonics_to_keep = 6  # Keep the first 6 harmonics, including the fundamental
fft_result_suppressed = fft_result.copy()
fft_result_suppressed[harmonics_to_keep:] = 0  # Set higher harmonics to zero

# Inverse FFT to get the time-domain signal after suppression
time_domain_signal_suppressed = np.fft.ifft(fft_result_suppressed).real

# Plot the original and suppressed signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.step(time, line_code, where='post', color='b', label='Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Original Signal vs. Suppressed Signal')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.step(time, time_domain_signal_suppressed, where='post', color='g', label='Suppressed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

