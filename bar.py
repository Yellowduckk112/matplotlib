import matplotlib.pyplot as plt
import numpy as np

n = 12
a = np.arange(n)
Y1 = (1 - a / float(n)) * np.random.uniform(0, 1, n)
Y2 = (1 - a / float(n)) * np.random.uniform(0, 1, n)
max1 = max(Y1)
max2 = max(Y2)
plt.bar(a, +Y1, label="blue")
plt.bar(a, -Y2, label="orange")
plt.legend()

for x, y in zip(a, Y2):
    plt.text(x-0.55, -y-0.15, "%.3f"%y)
for x, y in zip(a, Y1):
    plt.text(x-0.55, y+0.05, "%.3f"%y)

plt.xticks(())
plt.ylim(-max2 - 0.3, max1 + 0.3)

plt.show()