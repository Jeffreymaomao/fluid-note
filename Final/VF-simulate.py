import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 13,
    'text.usetex': True
})

def velocity_field(x, y):
    u_x = y**3 - 9*y
    u_y = x**3 - 9*x
    return np.array([u_x, u_y])

def rk4_step(position, dt):
    def velocity_at(pos):
        return velocity_field(pos[0], pos[1])
    
    k1 = dt * velocity_at(position)
    k2 = dt * velocity_at(position + 0.5 * k1)
    k3 = dt * velocity_at(position + 0.5 * k2)
    k4 = dt * velocity_at(position + k3)
    
    return position + (k1 + 2*k2 + 2*k3 + k4) / 6

def simulate_multiple_particles(initial_positions, t_max, dt):
    num_particles = initial_positions.shape[0]
    t = np.arange(0, t_max, dt)
    all_positions = np.zeros((num_particles, len(t), 2))

    for p in range(num_particles):
        all_positions[p, 0] = initial_positions[p]
        for i in range(1, len(t)):
            current_position = all_positions[p, i-1]
            velocity = velocity_field(current_position[0], current_position[1])
            new_position = rk4_step(current_position, dt)
            all_positions[p, i] = new_position

    return all_positions

# 初始位置（随机生成100个粒子的位置）
num_particles = 200
initial_positions = 4*(2 * np.random.rand(num_particles, 2) - 1)  # 粒子初始位置在[-10, 10]范围内
# 时间范围和步长
t_max = 2
dt = 0.005

# 运行模拟
all_positions = simulate_multiple_particles(initial_positions, t_max, dt)


fig, ax = plt.subplots(figsize=(6,6))
lim = 5
dticks = 2
desmos_red = (0.81, 0.22, 0.29, 1.0)
ticks = np.arange(-lim, lim+dticks, dticks)
arr = np.linspace(-lim*0.9,lim*0.9,20)
x,y = np.meshgrid(arr, arr)
u = y**3 - 9*y
v = x**3 - 9*x
scale = 5.0
uv_len = np.sqrt(u**2 + v**2)**0.6
u = scale * u / uv_len
v = scale * v / uv_len



particle_paths = [ax.plot([], [], '-', color=desmos_red, alpha=0.5, linewidth=0.5)[0] for _ in range(num_particles)]
particles = [ax.plot([], [], 'o', color=desmos_red)[0] for _ in range(num_particles)]
plt.quiver(x,y,u,v,color='royalblue', zorder=2)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.axis('equal')
plt.xlim(-lim-1, lim+1)
plt.ylim(-lim-1, lim+1)

def init():
    for path, particle in zip(particle_paths, particles):
        path.set_data([], [])
        particle.set_data([], [])
    return particle_paths + particles

def update(frame):
    for path, particle, positions in zip(particle_paths, particles, all_positions):
        path.set_data(positions[:frame, 0], positions[:frame, 1])
        particle.set_data(positions[frame, 0], positions[frame, 1])
    return particle_paths + particles

ani = FuncAnimation(fig, update, frames=len(all_positions[0]), init_func=init, blit=True, interval=10)

writer = FFMpegWriter(fps=30, metadata=dict(artist='Chang-Mao'), bitrate=100000)
ani.save("particle_motion.mp4", writer=writer)

# 显示动画
# plt.show()
