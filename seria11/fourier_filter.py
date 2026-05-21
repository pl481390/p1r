import argparse
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.default_rng()

"""y1 = np.sin(2*np.pi*t)
y2 = 0.5*np.cos(2*np.pi*2*t)
y3 = 0.25*np.sin(2*np.pi*3*t)

signal = y1 + y2 + y3"""

def signal_generator(sygnal_str, t):
    output = eval(sygnal_str)
    return output

def noise_generator(sygnal, sigma):
    return sygnal + rng.normal(loc=0.0, scale=sigma, size=len(sygnal))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("signal_str", type=str)
    parser.add_argument("f_probkowania", type=float)
    parser.add_argument("t_sygnalu", type=float)
    parser.add_argument("f_cutoff", type=float)
    parser.add_argument("sigma", type=float)
    args = parser.parse_args()

    t = np.linspace(0, args.t_sygnalu, int(args.t_sygnalu*args.f_probkowania))
    sygnal = signal_generator(args.signal_str, t)
    sygnal = noise_generator(sygnal, args.sigma)

    plt.plot(t, sygnal)
    plt.show()

    fft_result = np.fft.fft(sygnal)
    fft_freqs = np.fft.fftfreq(len(sygnal), 1/args.f_probkowania)
    plt.scatter(fft_freqs, np.abs(fft_result))
    plt.xlim(-20, 20)
    plt.show()

    #mask = np.abs(fft_freqs) > args.f_cutoff
    #fft_result[mask] = 0
    #odszumiony_sygnal = np.fft.ifft(fft_result)

    super_gaussian_window = np.exp(-0.5 * (fft_freqs/args.f_cutoff)**2)
    fft_result = fft_result*super_gaussian_window
    odszumiony_sygnal = np.fft.ifft(fft_result)

    plt.plot(t, odszumiony_sygnal)
    plt.show()