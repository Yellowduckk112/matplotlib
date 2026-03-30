import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 4, 0.1)
y = x*0.5

plt.figure()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['up'].set_color('none')
ax.spines['down'].set_color('none')