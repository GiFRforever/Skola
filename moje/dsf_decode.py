samples = []

with open("waveform.dsf", "rb") as file:
    while True:
        b = file.read(64)
        if b == b"":
            break
        temp = 0
        for i in b:
            temp += i
        
        samples.append(temp)

from matplotlib import pyplot as plt

plt.plot(samples)
plt.show()
