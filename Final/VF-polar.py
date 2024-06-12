import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})

arr = np.linspace(-9,9,20)
N = 5
ticks = np.linspace(-10,10,N)
x,y = np.meshgrid(arr, arr)

u = -y / np.sqrt(x**2 + y**2 + 1e-16) 
v =  x / np.sqrt(x**2 + y**2 + 1e-16) + 0.5 * np.sin(x + y)

scale = 2.0
uv_len = np.sqrt(u**2 + v**2) 
u = scale * u / uv_len
v = scale * v / uv_len

fig,ax = plt.subplots(figsize=(5,5))

# for _x,_y in zip(x.flatten(),y.flatten()):
#     ax.plot([0,_x],[0,_y], color='gray', linewidth=0.5, zorder=0)

# ax.scatter(x,y, color='royalblue')
# desmos_red = (0.81, 0.22, 0.29, 1.0)
ax.quiver(x,y,u,v,color='royalblue', zorder=1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-11,11)
ax.set_ylim(-11,11)
plt.show()

filename = "path-stream-with-time.pdf"
fig.savefig(f'assets/{filename}')


