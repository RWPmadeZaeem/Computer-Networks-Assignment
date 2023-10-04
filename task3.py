import numpy as np
import matplotlib.pyplot as plt

# Define a range of SNR values in dB (e.g., from -10 dB to 20 dB)
snr_db = np.linspace(-10, 20, 100)

# Convert SNR from dB to linear scale
snr_linear = 10**(snr_db / 10)

# Assuming a fixed bandwidth (B) of the channel
bandwidth = 1000  # 1 kHz bandwidth

# Calculate the achievable bit rate using Shannon's Capacity Formula
achievable_bit_rate = bandwidth * np.log2(1 + snr_linear)

# Plot SNR vs. achievable bit rate
plt.figure(figsize=(10, 6))
plt.plot(snr_db, achievable_bit_rate, color='b', linewidth=2, label='Achievable Bit Rate')
plt.xlabel('SNR (dB)')
plt.ylabel('Achievable Bit Rate (bps)')
plt.title('SNR vs. Achievable Bit Rate')
plt.grid(True)
plt.legend()
plt.show()
