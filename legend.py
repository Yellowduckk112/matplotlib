import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5, 0.1)
y1 = x*2+1
y2 = x**2+x

plt.figure()
plt.xlabel = "priority"
plt.ylabel = "yellowduckk"
plt.plot(x, y1, linestyle="--", label="world")
plt.plot(x, y2, color="red", label="hello")
plt.legend(loc="lower right")

plt.show()