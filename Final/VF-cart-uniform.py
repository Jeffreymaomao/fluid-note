import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})
lim = 5
dticks = 2

ticks = np.arange(-lim, lim+dticks, dticks)
arr = np.linspace(-lim*0.9,lim*0.9,20)
x,y = np.meshgrid(arr, arr)

u = -y
v = 0.0

scale = 5.0
uv_len = np.sqrt(u**2 + v**2)**0.6
u = scale * u / uv_len
v = scale * v / uv_len

fig,ax = plt.subplots(figsize=(5,5))
desmos_red = (0.81, 0.22, 0.29, 1.0)
ax.quiver(x,y,u,v,color='royalblue', zorder=1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-lim-1,lim+1)
ax.set_ylim(-lim-1,lim+1)
plt.show()

filename = "(-y,0).pdf"
fig.savefig(f'assets/{filename}')


