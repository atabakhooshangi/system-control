import numpy as np


def equations(state, a, b, c, u):
    x, y, z = state
    dx = a * y + u * x
    dy = -c * x + y * z + u * y
    dz = b - y ** 2 + u * z
    return np.array([dx, dy, dz])


def simulate_system(a, b, c, initial_conditions, time, dt):
    num_steps = len(time)
    state = np.array(initial_conditions)
    trajectory = np.zeros((num_steps, 3))

    for i in range(num_steps):
        trajectory[i] = state
        state += equations(state, a, b, c, u=0) * dt

    return trajectory.T
