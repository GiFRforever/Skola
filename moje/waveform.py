from math import sin, pi

freq = 440 # Hz
sample_rate = 44100 # Hz
dsd_sample_rate = 2_822_400 # Hz

period = 1 / freq # s
t = 0 # s
dt = 1 / sample_rate # s
sample_rate_ratio = dsd_sample_rate // sample_rate
number_of_samples = sample_rate // (freq * 2)
number_of_samples_dsd = dsd_sample_rate // (freq * 2)

print(f"period: {period} s")
print(f"dt: {dt} s")
print(f"sample_rate_ratio: {sample_rate_ratio}")
print(f"number_of_samples: {number_of_samples}")
print(f"number_of_samples_dsd: {number_of_samples_dsd}")

samples = [0 for _ in range(number_of_samples_dsd)]

for n in range(number_of_samples):
    amplitude = sin(2 * pi * freq * t)
    t += dt

    for s in range(sample_rate_ratio):
        mean = sum(samples[n * sample_rate_ratio : n * sample_rate_ratio + s]) / (s + 1)

        if amplitude > mean:
            samples[n * sample_rate_ratio + s] = 1
        else:
            samples[n * sample_rate_ratio + s] = 0

with open("waveform.dsf", "wb") as file:
    # file.write("DSD\n")
    # file.write("SAMPLE_RATE: {}\n".format(dsd_sample_rate))
    # file.write("SAMPLES: {}\n".format(number_of_samples_dsd))
    # file.write("CHANNELS: 1\n")
    # file.write("SAMPLE_WIDTH: 1\n")
    # file.write("END_HEADER\n")

    # for sample in samples:
    #     file.write("{}\n".format(sample))

    file.write(bytes(samples))

