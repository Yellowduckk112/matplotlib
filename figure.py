import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10, 0.1)
y1 = x*4
y2 = np.exp(x)

plt.figure(figsize=(4, 8))
plt.plot(x, y1, label="y=4x", color="red")

plt.figure(num=4, figsize=(4, 7))
plt.plot(x, y2, label="e^x", color='black')
plt.show()