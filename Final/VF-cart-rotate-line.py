import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps

from scipy.integrate import solve_ivp

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})

def rk4(f, x0, y0, h, n):
    t = np.zeros(n+1)
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0
    for i in range(1, n+1):
        k1x, k1y = f(x[i-1], y[i-1])
        k2x, k2y = f(x[i-1] + h/2*k1x, y[i-1] + h/2*k1y)
        k3x, k3y = f(x[i-1] + h/2*k2x, y[i-1] + h/2*k2y)
        k4x, k4y = f(x[i-1] + h*k3x, y[i-1] + h*k3y)
        x[i] = x[i-1] + h/6*(k1x + 2*k2x + 2*k3x + k4x)
        y[i] = y[i-1] + h/6*(k1y + 2*k2y + 2*k3y + k4y)
    return x, y

def f(x, y):
    dxdt = -y
    dydt = 0.0*x
    return dxdt, dydt

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

x_sols = []
y_sols = []

N_grid = 50
y_grid = np.linspace(0.0, lim*0.9, N_grid)
x0 = 0.0

for y0 in y_grid:
    x_sol, y_sol = rk4(f, x0, y0, 0.005, 200)
    x_sols.append(x_sol)
    y_sols.append(y_sol)

x_sols = np.array(x_sols)
y_sols = np.array(y_sols)

jet = colormaps['jet']

fig,ax = plt.subplots(figsize=(6,5))
ax.set_title(r'Plot path line for $t=0\sim 1$')
desmos_red = (0.81, 0.22, 0.29, 1.0)
desmos_blue = 'royalblue'
ax.quiver(x,y,u,v,color=desmos_blue, zorder=2)


n_color = len(x_sols.T)
for i, (x_sol, y_sol) in enumerate(zip(x_sols.T, y_sols.T)):
    color = jet(i/n_color)
    if(i%6): continue
    ax.plot(x_sol, y_sol, '-',color=color, linewidth=0.5, zorder=1)
    ax.scatter(x_sol, y_sol, color=color, s=0.4)


# for i, (x_sol, y_sol) in enumerate(zip(x_sols, y_sols)):
#     ax.plot(x_sol, y_sol, '-',color=desmos_red, linewidth=0.5, zorder=1)


# ax.scatter(x_sols[:,0], y_sols[:,0], color=desmos_red, s=2)

sm = plt.cm.ScalarMappable(cmap=jet)
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('time $t$')

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-lim-1,1)
ax.set_ylim(-1,lim+1)
plt.show()

filename = "flow-(-y,0)-path-links-color.pdf"
# filename = "flow-(-y,0)-path-stick.pdf"
fig.savefig(f'assets/{filename}')


