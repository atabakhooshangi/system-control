import numpy as np
import matplotlib.pyplot as plt


def control_simulation():
    # Control parameters
    Lambda = 3
    K = 500
    w = 1

    # PID gains
    Kp = Lambda
    Ki = 0.1 * Lambda
    Kd = 0.01 * Lambda

    # Time setup
    dt = 1e-3
    T = 2e4
    times = np.arange(0, T * dt, dt)

    # Parameters
    a = 9  # Approximate values for control
    b = 98
    c = 0.4

    # Nominal trajectory parameters
    A1, omega1 = 2, 0.5
    A2, omega2 = 3.8, 0.7
    A3, omega3 = 1.5, 0.9

    # Desired trajectories
    x_desired = A1 * np.sin(omega1 * times)
    y_desired = A2 * np.sin(omega2 * times)
    z_desired = A3 * np.sin(omega3 * times)

    # Initial conditions
    x, y, z = np.zeros(len(times)), np.zeros(len(times)), np.zeros(len(times))
    x_dot, y_dot, z_dot = np.zeros(len(times)), np.zeros(len(times)), np.zeros(len(times))
    u_x, u_y, u_z = np.zeros(len(times)), np.zeros(len(times)), np.zeros(len(times))

    x[0], y[0], z[0] = 0.0, 0.0, 0.0  # All initial conditions are zero as per task

    # Control error metrics
    error_x, integral_x, derivative_x = np.zeros(len(times)), np.zeros(len(times)), np.zeros(len(times))
    error_y, integral_y, derivative_y = np.zeros(len(times)), np.zeros(len(times)), np.zeros(len(times))
    error_z, integral_z, derivative_z = np.zeros(len(times)), np.zeros(len(times)), np.zeros(len(times))

    # Simulation loop
    for i in range(len(times) - 1):
        # PID Error calculations
        error_x[i] = x_desired[i] - x[i]
        integral_x[i] += error_x[i] * dt
        derivative_x[i] = (error_x[i] - error_x[i - 1]) / dt if i > 0 else 0.0
        u_x[i] = Kp * error_x[i] + Ki * integral_x[i] + Kd * derivative_x[i]

        error_y[i] = y_desired[i] - y[i]
        integral_y[i] += error_y[i] * dt
        derivative_y[i] = (error_y[i] - error_y[i - 1]) / dt if i > 0 else 0.0
        u_y[i] = Kp * error_y[i] + Ki * integral_y[i] + Kd * derivative_y[i]

        error_z[i] = z_desired[i] - z[i]
        integral_z[i] += error_z[i] * dt
        derivative_z[i] = (error_z[i] - error_z[i - 1]) / dt if i > 0 else 0.0
        u_z[i] = Kp * error_z[i] + Ki * integral_z[i] + Kd * derivative_z[i]

        # Update state using the system dynamics with control inputs
        x_dot[i] = a * y[i] + np.tanh(u_x[i] / w)
        y_dot[i] = -c * x[i] + y[i] * z[i] + np.tanh(u_y[i] / w)
        z_dot[i] = b - y[i] ** 2 + np.tanh(u_z[i] / w)

        x[i + 1] = x[i] + dt * x_dot[i]
        y[i + 1] = y[i] + dt * y_dot[i]
        z[i + 1] = z[i] + dt * z_dot[i]

    # Plotting
    plot_results(times, x_desired, y_desired, z_desired, x, y, z, error_x, error_y, error_z, x_dot, y_dot, z_dot, u_x,
                 u_y, u_z)


def plot_results(times, x_desired, y_desired, z_desired, x, y, z, error_x, error_y, error_z, x_dot, y_dot, z_dot, u_x,
                 u_y, u_z):
    # Figure 1: Nominal and Realized Trajectories & Tracking Errors
    plt.figure(figsize=(12, 8))

    plt.subplot(321)
    plt.title("Nominal and Realized Trajectories for x")
    plt.plot(times, x_desired, "r--", label="Nominal x")
    plt.plot(times, x, "b", label="Realized x")
    plt.legend()

    plt.subplot(322)
    plt.title("Tracking Error for x")
    plt.plot(times, error_x, label="Error x")
    plt.legend()

    plt.subplot(323)
    plt.title("Nominal and Realized Trajectories for y")
    plt.plot(times, y_desired, "r--", label="Nominal y")
    plt.plot(times, y, "b", label="Realized y")
    plt.legend()

    plt.subplot(324)
    plt.title("Tracking Error for y")
    plt.plot(times, error_y, label="Error y")
    plt.legend()

    plt.subplot(325)
    plt.title("Nominal and Realized Trajectories for z")
    plt.plot(times, z_desired, "r--", label="Nominal z")
    plt.plot(times, z, "b", label="Realized z")
    plt.legend()

    plt.subplot(326)
    plt.title("Tracking Error for z")
    plt.plot(times, error_z, label="Error z")
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Figure 2: Phase Space & Control Signals
    plt.figure(figsize=(12, 8))

    plt.subplot(321)
    plt.title("Phase Space for x")
    plt.plot(x, x_dot, label="Phase x")
    plt.legend()

    plt.subplot(322)
    plt.title("Control Signal for x")
    plt.plot(times, u_x, label="Control u_x")
    plt.legend()

    plt.subplot(323)
    plt.title("Phase Space for y")
    plt.plot(y, y_dot, label="Phase y")
    plt.legend()

    plt.subplot(324)
    plt.title("Control Signal for y")
    plt.plot(times, u_y, label="Control u_y")
    plt.legend()

    plt.subplot(325)
    plt.title("Phase Space for z")
    plt.plot(z, z_dot, label="Phase z")
    plt.legend()

    plt.subplot(326)
    plt.title("Control Signal for z")
    plt.plot(times, u_z, label="Control u_z")
    plt.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    control_simulation()
