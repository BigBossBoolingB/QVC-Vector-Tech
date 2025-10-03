# Chronos Prototype: Ethical Matrix for Physical Systems

This project is a foundational software prototype demonstrating the core safety principles of the **Chronos Ecosystem**, specifically tailored for cyber-physical systems. It implements the concept of an **Ethical Matrix** and **Project Failsafe** to govern the actions of a simulated robot, ensuring its behavior remains within a predefined set of constitutional safety rules.

## Core Concept

The prototype is built on the idea that any action proposed by an autonomous system (the "Cognitive Vector") must be validated against a set of immutable laws (the "Ethical Matrix") before it can be executed in the physical world. This ensures that the system operates safely and predictably, preventing harmful or destructive outcomes.

## Project Structure

The project is organized into the following directories and files:

- **`main.py`**: The main entry point for the simulation. It initializes the system, defines the safety rules, and runs several demonstration scenarios.

- **`src/`**: Contains the core source code.
  - **`core/qvc.py`**: Defines the fundamental data structures for the simulation, such as `Vector3`, `SystemState`, and `ActionVector`. These represent the state and proposed actions of physical objects.
  - **`physical/robot.py`**: Contains the `Robot` class, a simple simulation of a physical agent that has a state and can perform actions.
  - **`ethical/`**: Implements the Ethical Matrix.
    - **`constitution.py`**: Defines the `ConstitutionalKnowledgeBase`, which holds the set of machine-readable safety rules (e.g., maximum velocity, forbidden zones).
    - **`failsafe.py`**: Implements `ProjectFailsafe`, the core validation engine that checks proposed actions against the constitution.
  - **`cognitive/`**: (Placeholder) In a full implementation, this would house the complex AI/ML models that propose actions.
  - **`creative/`**: (Placeholder) In a full implementation, this would house generative algorithms for novel problem-solving.

## How to Run the Demonstration

To run the simulation, follow these steps:

1.  **Install Dependencies**: The project requires `numpy`.
    ```bash
    pip install numpy
    ```

2.  **Run the Script**: Execute the `main.py` file from the root directory.
    ```bash
    python3 main.py
    ```

## Understanding the Output

The script will run three scenarios to demonstrate `ProjectFailsafe` in action:

1.  **Scenario 1: Safe Action**
    - The robot proposes a move that is within the speed limit and does not enter any forbidden zones.
    - `ProjectFailsafe` validates the action as **SAFE**.
    - The robot's state is updated.

2.  **Scenario 2: Unsafe Action (Max Velocity Violation)**
    - The robot proposes to move at a speed that exceeds the `MaxVelocityRule`.
    - `ProjectFailsafe` identifies the violation and validates the action as **UNSAFE**.
    - The action is aborted, and the robot's state does not change.

3.  **Scenario 3: Unsafe Action (Forbidden Zone Violation)**
    - The robot proposes a move with a safe velocity, but its predicted trajectory over a few seconds leads into a `ForbiddenZoneRule`.
    - `ProjectFailsafe` predicts the illegal entry and validates the action as **UNSAFE**.
    - The action is aborted, and the robot's state remains unchanged.