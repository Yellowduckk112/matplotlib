import matplotlib.pyplot as plt
import numpy as np

n = 100
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

plt.figure()
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
t = np.arctan2(x, y)
plt.scatter(x, y, s=45, c=t, alpha=0.3)

plt.show()