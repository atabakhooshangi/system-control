# System and Control Project

## Overview
This project simulates a dynamic system given by a set of differential equations and implements a Variable Structure/Sliding Mode control system with PID error metrics. The project uses Python with `numpy` and `matplotlib`.

## Files
- **main.py**: Main script to run the simulation and control system.
- **simulation.py**: Functions for simulating the system.
- **control.py**: Functions for control law and controlled simulation.
- **plots.py**: Functions for plotting results.
- **requirements.txt**: Required Python packages.

## Usage
1. Ensure you have Python installed along with `numpy` and `matplotlib`.
2. Install the required packages using:
    ```bash
    pip install -r requirements.txt
    ```
3. To run Task 1: Simulate the system without control, execute:
    ```bash
    python main.py 1
    ```
4. To run Task 2: Simulate the system with control, execute:
    ```bash
    python main.py 2
    ```

## Description
- **Task 1**: The system is simulated without control using the given initial conditions.
- **Task 2**: The system is simulated with a VS/SM control system using PID error metrics. Various plots are generated, including nominal and realized trajectories, tracking errors, phase spaces, and control signals.
