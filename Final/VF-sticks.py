import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

# 定义速度场
def velocity_field(x, y):
    u_x = y**3 - 9*y
    u_y = x**3 - 9*x
    return np.array([u_x, u_y])

# RK4 方法更新位置
def rk4_step(position, dt):
    def velocity_at(pos):
        return velocity_field(pos[0], pos[1])
    
    k1 = dt * velocity_at(position)
    k2 = dt * velocity_at(position + 0.5 * k1)
    k3 = dt * velocity_at(position + 0.5 * k2)
    k4 = dt * velocity_at(position + k3)
    
    return position + (k1 + 2*k2 + 2*k3 + k4) / 6

# 模拟棍子的运动
def simulate_stick_motion(initial_position, initial_angle, length, t_max, dt):
    t = np.arange(0, t_max, dt)
    positions = np.zeros((len(t), 2))
    angles = np.zeros(len(t))
    positions[0] = initial_position
    angles[0] = initial_angle
    
    for i in range(1, len(t)):
        # 更新质心位置
        current_position = positions[i-1]
        new_position = rk4_step(current_position, dt)
        positions[i] = new_position
        
        # 更新旋转角度
        x1, y1 = current_position + (length / 2) * np.array([np.cos(angles[i-1]), np.sin(angles[i-1])])
        x2, y2 = current_position - (length / 2) * np.array([np.cos(angles[i-1]), np.sin(angles[i-1])])
        v1 = velocity_field(x1, y1)
        v2 = velocity_field(x2, y2)
        dv = v1 - v2
        angular_velocity = np.linalg.norm(dv) / length  # 简化的角速度计算
        new_angle = angles[i-1] + angular_velocity * dt
        angles[i] = new_angle
    
    return positions, angles

# 初始条件
initial_position = np.array([2, 1])
initial_angle = np.pi / 4  # 45度
length = 2
t_max = 10
dt = 0.01

# 运行模拟
positions, angles = simulate_stick_motion(initial_position, initial_angle, length, t_max, dt)

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(np.min(positions[:,0])-1, np.max(positions[:,0])+1)
ax.set_ylim(np.min(positions[:,1])-1, np.max(positions[:,1])+1)

stick, = ax.plot([], [], 'b-', lw=2)
plt.title('Stick Motion in Given Velocity Field')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# 初始化函数
def init():
    stick.set_data([], [])
    return stick,

# 动画更新函数
def update(frame):
    x1 = positions[frame] + (length / 2) * np.array([np.cos(angles[frame]), np.sin(angles[frame])])
    x2 = positions[frame] - (length / 2) * np.array([np.cos(angles[frame]), np.sin(angles[frame])])
    stick.set_data([x1[0], x2[0]], [x1[1], x2[1]])
    return stick,

# 创建动画
ani = FuncAnimation(fig, update, frames=len(positions), init_func=init, blit=True, interval=10)

# 保存动画到MP4文件，设置高质量参数
writer = FFMpegWriter(fps=30, metadata=dict(artist='Me'), codec='libx264', bitrate=5000)
ani.save("stick_motion.mp4", writer=writer)

plt.show()
