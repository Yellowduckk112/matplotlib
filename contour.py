import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return (x**2+y**2)

n = 512
x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)
plt.contourf(X, Y, f(X, Y), 8, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 8, colors="black", linewidth=0.5)
plt.clabel(C, inline=True, fontsize=10)

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.show()