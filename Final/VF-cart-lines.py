import numpy as np
import matplotlib.pyplot as plt

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

def streamline_ode(x, y):
    u_x, u_y = f(x, y)
    return u_y / u_x

def compute_streamline(start_point, t_max, dt):
    def rhs(t, z):
        x, y = z
        u_x, u_y = f(x, y)
        return [u_x, u_y]

    t_eval = np.arange(0, t_max, dt)
    sol = solve_ivp(rhs, [0, t_max], start_point, t_eval=t_eval, vectorized=True)
    return sol.y[0], sol.y[1]

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

x_streams = []
y_streams = []

N_grid = 500
x_grid = 6.0 * (2.0 * np.random.random(N_grid)-1.0)
y_grid = 6.0 * (2.0 * np.random.random(N_grid)-1.0)

# x_grid = x.flatten()
# y_grid = y.flatten()

for x0, y0 in zip(x_grid, y_grid):
    x_stream, y_stream = compute_streamline([x0, y0], 1, 0.01)
    x_streams.append(x_stream)
    y_streams.append(y_stream)



# for x0, y0 in zip(x_grid, y_grid):
#     x_sol, y_sol = rk4(f, x0, y0, 0.005, 300)
#     x_sols.append(x_sol)
#     y_sols.append(y_sol)

fig,ax = plt.subplots(figsize=(5,5))
desmos_red = (0.81, 0.22, 0.29, 1.0)
desmos_blue = 'royalblue'
ax.quiver(x,y,u,v,color='black', zorder=2)

# for x_sol, y_sol in zip(x_sols, y_sols):
    # ax.plot(x_sol, y_sol, '-',color=desmos_red, linewidth=0.1, zorder=1)

for x_stream, y_stream in zip(x_streams, y_streams):
    ax.plot(x_stream, y_stream, '-',color=desmos_blue, linewidth=0.1, zorder=1)

ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-lim-1,lim+1)
ax.set_ylim(-lim-1,lim+1)
plt.show()

filename = "(-y,0)-stream.pdf"
fig.savefig(f'assets/{filename}')


