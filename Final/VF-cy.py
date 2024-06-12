import numpy as np
import matplotlib.pyplot as plt

SAVE_FIG = False

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})

# 定义网格
r = np.linspace(0, 9, 5)
theta = np.linspace(0, 2*np.pi, 20)
z = np.linspace(-9, 9, 10)
R, Theta, Z = np.meshgrid(r, theta, z)

A_r = R / (np.sqrt(R**2 + 1e-16))
A_theta = Theta * 0.0 + 1.0
A_z = Z * 0.0

X = R * np.cos(Theta)
Y = R * np.sin(Theta)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, A_r * np.cos(Theta) - A_theta * np.sin(Theta),
          A_r * np.sin(Theta) + A_theta * np.cos(Theta), A_z,
          length=1.5, cmap='jet')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

plt.show()

if SAVE_FIG and fig:
    filename = input('filename: ')
    fig.savefig(f'assets/{filename}.svg')