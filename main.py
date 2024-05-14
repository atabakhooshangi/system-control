import sys
import numpy as np
from simulation import simulate_system
from control import simulate_controlled_system
from plots import (
    plot_3d_trajectory,
    plot_time_series_separate,
    plot_nominal_realized_trajectories,
    plot_tracking_errors,
    plot_phase_spaces,
    plot_control_signals
)


def main(ctrl):
    # Parameters
    a, b, c = 10, 100, 0.3
    T = int(2e4)
    dt = 1e-3
    time = np.arange(0, T * dt, dt)

    if ctrl == '1':
        # Simulate the system without control
        initial_conditions = [0.1, 0.1, 0.1]
        x, y, z = simulate_system(a, b, c, initial_conditions, time, dt)
        plot_3d_trajectory(x, y, z)
        plot_time_series_separate(time, x, y, z)

    elif ctrl == '2':
        # Simulate the system with control
        A = [2, 3.8, 1.5]
        w = [0.5, 0.7, 0.9]
        nominal_trajectory = [A[i] * np.sin(w[i] * time) for i in range(3)]

        control_initial_conditions = [0.0, 0.0, 0.0]
        params = {'Kp': 3, 'Ki': 0.3, 'Kd': 0.03}  # Example PID parameters

        x_c, y_c, z_c, control_signals, tracking_errors = simulate_controlled_system(
            a, b, c, control_initial_conditions, nominal_trajectory, params, time, dt
        )

        plot_time_series_separate(time, x_c, y_c, z_c)
        plot_nominal_realized_trajectories(time, nominal_trajectory, x_c, y_c, z_c)
        plot_tracking_errors(time, tracking_errors)
        plot_phase_spaces(x_c, y_c, z_c)
        plot_control_signals(time, control_signals)
    else:
        print("Invalid task. Please choose '1' or '2'.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <option>")
        print("Option 1: Simulate system without control")
        print("Option 2: Simulate system with control")
    else:
        option = sys.argv[1]
        main(option)
