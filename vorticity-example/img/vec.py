import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})

arr = np.linspace(-9,9,15)
dx = arr[1] - arr[0]
print(dx)
N = 5
ticks = np.linspace(-10,10,N)
x,y = np.meshgrid(arr, arr)

u = -y / (x**2 + y**2 + 1e-16)
v =  x / (x**2 + y**2 + 1e-16)

magnitude = np.sqrt(u**2 + v**2+ 1e-16)
u_n = u/magnitude
v_n = v/magnitude
fig,ax = plt.subplots()
ax.set_title(r'velocity vector field $\textbf{u}$')
ax.scatter(x, y, color='gray', s=5)
quiv = ax.quiver(x, y, u_n, v_n, magnitude,
    cmap='jet',
    scale=1.0/0.05)

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.axis('equal')
plt.colorbar(quiv, ax=ax)
plt.show()

filename = input('filename: ')
fig.savefig(f'./{filename}.pdf')


