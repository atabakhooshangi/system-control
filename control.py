import numpy as np


def control_law(state, desired_state, prev_error, integral, dt, params):
    # PID control law
    Kp = params['Kp']
    Ki = params['Ki']
    Kd = params['Kd']

    error = np.array(desired_state) - np.array(state)
    integral += error * dt
    derivative = (error - prev_error) / dt

    control_signal = Kp * error + Ki * integral + Kd * derivative
    return control_signal, error, integral


def controlled_equations(state, a, b, c, control_signal):
    x, y, z = state
    u = control_signal
    dx = a * y + np.tanh(u[0])
    dy = -c * x + y * z + np.tanh(u[1])
    dz = b - y ** 2 + np.tanh(u[2])
    return np.array([dx, dy, dz])


def simulate_controlled_system(a, b, c, initial_conditions, desired_trajectory, params, time, dt):
    num_steps = len(time)
    state = np.array(initial_conditions)
    trajectory = np.zeros((num_steps, 3))
    control_signals = np.zeros((num_steps, 3))
    tracking_errors = np.zeros((num_steps, 3))
    integral = np.zeros(3)
    prev_error = np.zeros(3)

    for i in range(num_steps):
        desired_state = [traj[i] for traj in desired_trajectory]
        control_signal, error, integral = control_law(state, desired_state, prev_error, integral, dt, params)
        prev_error = error

        control_signals[i] = control_signal
        tracking_errors[i] = error
        trajectory[i] = state
        state += controlled_equations(state, a, b, c, control_signal) * dt

    x, y, z = trajectory.T
    return x, y, z, control_signals.T, tracking_errors.T
