import numpy as np
import matplotlib.pyplot as plt
import glob

# this analyzes our fake data
files = glob.glob("data/*.csv")
fig = []

# load our code
for i in files[0:3]:
    data = np.loadtxt(files[i], delimiter=",")
    fig.append(plt.figure("our title " + str(i), figsize=(10.0, 3.0)))

    axes1 = fig[i].add_subplot(1, 3, 1)
    axes1.plot(data.mean(axis=0))
    axes1.set_ylabel("average")

    axes2 = fig[i].add_subplot(1, 3, 2)
    axes2.plot(data.max(axis=0))
    axes2.set_ylabel("max")

    axes3 = fig[i].add_subplot(1, 3, 3)
    axes3.plot(data.min(axis=0))
    axes3.set_ylabel("min")

    fig[i].tight_layout()

# show the plot
plt.show()
