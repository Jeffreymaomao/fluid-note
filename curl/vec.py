import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})

arr = np.linspace(-9,9,15)
N = 5
ticks = np.linspace(-10,10,N)
x,y = np.meshgrid(arr, arr)

u = x / np.sqrt(x**2 + y**2 + 1e-16)
v = y / np.sqrt(x**2 + y**2 + 1e-16)

u = x*0.0 + 1.0
v = y*0.0 + 0.0

scale = 3
fig,ax = plt.subplots(figsize=(5,5))
ax.quiver(x,y,u,v,color='royalblue')

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
plt.show()

filename = input('filename: ')
fig.savefig(f'assets/{filename}.svg')


