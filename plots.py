import matplotlib.pyplot as plt


def plot_3d_trajectory(x, y, z):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3D Plot of the System Trajectory')
    plt.show()


def plot_time_series_separate(time, x, y, z):
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    axs[0].plot(time, x, label='x')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('x')
    axs[0].legend()
    axs[0].set_title('Time Plot for x')

    axs[1].plot(time, y, label='y')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('y')
    axs[1].legend()
    axs[1].set_title('Time Plot for y')

    axs[2].plot(time, z, label='z')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('z')
    axs[2].legend()
    axs[2].set_title('Time Plot for z')

    plt.tight_layout()
    plt.show()


def plot_nominal_realized_trajectories(time, nominal, x, y, z):
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    axs[0].plot(time, nominal[0], "r--", label='Nominal x')
    axs[0].plot(time, x, "b", label='Realized x')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Trajectory x')
    axs[0].legend()
    axs[0].set_title('Nominal and Realized Trajectories for x')

    axs[1].plot(time, nominal[1], "r--", label='Nominal y')
    axs[1].plot(time, y, "b", label='Realized y')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Trajectory y')
    axs[1].legend()
    axs[1].set_title('Nominal and Realized Trajectories for y')

    axs[2].plot(time, nominal[2], "r--", label='Nominal z')
    axs[2].plot(time, z, "b", label='Realized z')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Trajectory z')
    axs[2].legend()
    axs[2].set_title('Nominal and Realized Trajectories for z')

    plt.tight_layout()
    plt.show()


def plot_tracking_errors(time, tracking_errors):
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    axs[0].plot(time, tracking_errors[0], label='Error x')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Tracking Error x')
    axs[0].legend()
    axs[0].set_title('Tracking Error for x')

    axs[1].plot(time, tracking_errors[1], label='Error y')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Tracking Error y')
    axs[1].legend()
    axs[1].set_title('Tracking Error for y')

    axs[2].plot(time, tracking_errors[2], label='Error z')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Tracking Error z')
    axs[2].legend()
    axs[2].set_title('Tracking Error for z')

    plt.tight_layout()
    plt.show()


def plot_phase_spaces(x, y, z):
    fig, axs = plt.subplots(2, 1, figsize=(10, 12))

    axs[0].plot(x, y, label='x-y phase space')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('y')
    axs[0].legend()
    axs[0].set_title('Phase Space x-y')

    axs[1].plot(x, z, label='x-z phase space')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('z')
    axs[1].legend()
    axs[1].set_title('Phase Space x-z')

    # axs[2].plot(y, z, label='y-z phase space')
    # axs[2].set_xlabel('y')
    # axs[2].set_ylabel('z')
    # axs[2].legend()
    # axs[2].set_title('Phase Space y-z')

    plt.tight_layout()
    plt.show()

    # Single show
    plt.figure()
    plt.plot(y, z, label='y-z phase space')
    plt.xlabel('y')
    plt.ylabel('z')
    plt.title('Phase Space y-z')
    plt.legend()
    plt.show()


def plot_control_signals(time, control_signals):
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))

    axs[0].plot(time, control_signals[0], label='Control Signal x')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Control Signal x')
    axs[0].legend()
    axs[0].set_title('Control Signal for x')

    axs[1].plot(time, control_signals[1], label='Control Signal y')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Control Signal y')
    axs[1].legend()
    axs[1].set_title('Control Signal for y')

    axs[2].plot(time, control_signals[2], label='Control Signal z')
    axs[2].set_xlabel('Time')
    axs[2].set_ylabel('Control Signal z')
    axs[2].legend()
    axs[2].set_title('Control Signal for z')

    plt.tight_layout()
    plt.show()
