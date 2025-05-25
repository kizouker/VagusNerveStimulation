import numpy as np
import matplotlib.pyplot as plt

fs = 1000  # 1000 Hz sampling, dvs 1 ms upplösning
T = 2  # total tid i sekunder
t = np.linspace(0, T, int(T * fs))

# Skapa tom signal
signal = np.zeros_like(t)

# Tidpunkter (i sekunder) då pulser startar
start_times = [0.2, 0.4, 0.6, 0.9]  # När varje puls börjar

# Längder i millisekunder
lengths_ms = [50, 100, 200, 400]
lengths_s = [l / 1000 for l in lengths_ms]  # till sekunder

# Bygg signalen med diskreta Heaviside-kliv
for start, dur in zip(start_times, lengths_s):
    signal += (t >= start) & (t < start + dur)

# Plot
plt.figure(figsize=(10, 3))
plt.plot(t, signal)
plt.title("Diskret Heaviside-pulssekvens (U(t)-liknande)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()
