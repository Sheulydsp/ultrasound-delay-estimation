import numpy as np
from scipy.signal import ellip, filtfilt, tukey

# -------------------------------
# PARAMETERS
# -------------------------------
def set_parameters():
    p = {}
    p["fs"] = 1000
    p["fc"] = 5
    p["num_channels"] = 4
    p["max_delay"] = 0.01
    p["noise_level"] = 0.1
    p["num_trials"] = 20
    return p


# -------------------------------
# SIGNAL GENERATION
# -------------------------------
def generate_reference_signal(p):
    t = np.linspace(0, 1, p["fs"])
    signal = np.sin(2 * np.pi * p["fc"] * t)
    signal *= np.hamming(len(signal))
    return signal, t


# -------------------------------
# DELAY MODEL
# -------------------------------
def generate_delayed_signals(signal, p):
    delays = (2 * np.random.rand(p["num_channels"]) - 1) * p["max_delay"]
    delayed_signals = []

    for d in delays:
        shift = int(d * p["fs"])
        delayed = np.roll(signal, shift)
        delayed_signals.append(delayed)

    return np.array(delayed_signals), delays


# -------------------------------
# NOISE
# -------------------------------
def add_noise(signals, p):
    noise = p["noise_level"] * np.random.randn(*signals.shape)
    return signals + noise


# -------------------------------
# FILTER
# -------------------------------
def bandpass_filter(signal, fs):
    nyq = fs / 2
    b, a = ellip(4, 1, 30, [1/nyq, 10/nyq], btype='band')
    return filtfilt(b, a, signal)


# -------------------------------
# WINDOWING
# -------------------------------
def apply_taper(signal):
    window = tukey(len(signal), 0.8)
    return signal * window


# -------------------------------
# DELAY ESTIMATION
# -------------------------------
def estimate_delay(ref_signal, signal):
    corr = np.correlate(signal, ref_signal, mode='full')
    lags = np.arange(-len(ref_signal)+1, len(ref_signal))

    peak_idx = np.argmax(corr)
    delay = lags[peak_idx]

    # Parabolic interpolation
    if 0 < peak_idx < len(corr) - 1:
        y1 = corr[peak_idx - 1]
        y2 = corr[peak_idx]
        y3 = corr[peak_idx + 1]

        denom = (y1 - 2*y2 + y3)
        if denom != 0:
            delay += (y1 - y3) / (2 * denom)

    return delay


# -------------------------------
# MONTE CARLO SIMULATION
# -------------------------------
def run_simulation(p):

    errors = []

    for _ in range(p["num_trials"]):

        # Step 1: Reference signal
        ref_signal, _ = generate_reference_signal(p)

        # Step 2: Delays
        delayed_signals, true_delays = generate_delayed_signals(ref_signal, p)

        # Step 3: Add noise
        noisy_signals = add_noise(delayed_signals, p)

        # Step 4: Process each channel
        estimated = []

        for sig in noisy_signals:
            filtered = bandpass_filter(sig, p["fs"])
            tapered = apply_taper(filtered)
            est = estimate_delay(ref_signal, tapered)
            estimated.append(est / p["fs"])  # convert to time

        estimated = np.array(estimated)

        # Step 5: Error
        error = estimated - true_delays
        errors.append(error)

    errors = np.array(errors)

    # Statistics
    mean_error = np.mean(errors)
    std_error = np.std(errors)

    print("Mean error:", mean_error)
    print("Std deviation:", std_error)


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    params = set_parameters()
    run_simulation(params)