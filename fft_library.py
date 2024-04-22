import numpy as np
import matplotlib.pyplot as plt
def check_power_of_two(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def fft(x):
    N = len(x)
    if not check_power_of_two(N):
        raise ValueError("N is not a power of 2")
    if N <= 1: 
        return x
    elif N <= 2:
        return [x[0] + x[1], x[0] - x[1]]
   
    else:
        even = fft(x[::2])
        odd = fft(x[1::2])
        T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]
    

def calculate_frequencies(N, fs):
    freqs = []
    for i in range(N//2):
        freqs.append(i * fs / N)
    return freqs


def ifft(data):
    N = len(data)
    if N == 1:
        return data
    even = ifft(data[0::2])
    odd = ifft(data[1::2])
    T = [np.exp(2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def plot_freq_spectrum(fft_result, fs):
    N = len(fft_result)
    freqs = calculate_frequencies(N, fs)
    plt.plot(freqs, np.abs(fft_result[:N//2]))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.savefig("fft_spectrum.png")