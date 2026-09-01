import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# Signal frequency in Hz
f = 5

# Duration in seconds
duration = 1

# "Continuous" reference signal
# 1000 points makes it look smooth
t = np.linspace(0, duration, 1000)

# Generate the 5 Hz sine wave
signal = np.sin(2 * np.pi * f * t)

# Try different sampling frequencies
for fs in [100, 20, 10, 5]:

    # Sample instants
    ts = np.arange(0, duration, 1 / fs)

    # Sampled values
    samples = np.sin(2 * np.pi * f * ts)

    # Create figure
    plt.figure(figsize=(8, 3))

    # Original continuous-looking signal
    plt.plot(
        t,
        signal,
        color="lightgray",
        label="Original 5 Hz signal"
    )

    # Sample points
    plt.stem(
        ts,
        samples,
        linefmt="C0-",
        markerfmt="C0o",
        basefmt=" "
    )

    # Connect sampled points
    plt.plot(
        ts,
        samples,
        "r--",
        label=f"Samples from fs={fs} Hz"
    )

    plt.title(
        f"fs = {fs} Hz\n"
        f"(Nyquist requires fs > 10 Hz)"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.legend()
    plt.tight_layout()
    plt.show()
