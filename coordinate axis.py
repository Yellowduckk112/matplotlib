import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 4, 0.1)
y = x**3+3*x

plt.figure()
plt.plot(x, y, linewidth=1.5)
plt.xlabel("xxxx")
plt.ylabel("yyyy")
plt.xlim((-1, 4))
plt.ylim((-20, 70))

ticks = np.arange(-1, 4, 0.5)
plt.xticks(ticks)

ax = plt.gca()
ax.spines["bottom"].set_position(("data", -1))
plt.show()