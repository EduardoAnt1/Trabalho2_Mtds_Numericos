import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("1D heat equation solver")

plate_length = 10
max_iter_time = 750

alpha = 0.835
delta_x = 2
delta_t = 0.1
gamma = (alpha * delta_t) / (delta_x ** 2)

# Initialize solution: the grid of u(k, i)
u = np.empty((max_iter_time, plate_length))

# Initial condition everywhere inside the grid
u_initial = 0

# Boundary conditions
u_left = 100.0
u_right = 100.0
# Set the initial condition
u.fill(u_initial)

# Set the boundary conditions
u[:, 0] = u_left
u[:, -1] = u_right

def calculate(u):
    for k in range(max_iter_time - 1):
        print(k)
        for i in range(1, plate_length - 1):
            u[k + 1, i] = gamma * (u[k, i + 1] + u[k, i - 1] - 2 * u[k, i]) + u[k, i]

    return u

def plotheatmap(u_k, k):
    plt.clf()
    plt.title(f"Temperature at t = {k * delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("Temperature")
    plt.plot(u_k, color='b')
    plt.ylim(0, 100)  # Adjust this if needed
    plt.grid(True)

    return plt

# Perform the calculation
u = calculate(u)

def animate(k):
    plotheatmap(u[k], k)

fig = plt.figure()
anim = animation.FuncAnimation(fig, animate, interval=50, frames=max_iter_time, repeat=False)
anim.save("heat_equation_1D_solution.gif")

print("Done!")
