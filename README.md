# Chronos Prototype: Cognitive & Ethical Integration

This project is a software prototype demonstrating the core principles of the **Chronos Ecosystem**, focusing on the interaction between the **Cognitive Vector** and the **Ethical Matrix** for governing cyber-physical systems.

## Core Concept

The prototype demonstrates a complete feedback loop for autonomous action:
1.  The **Cognitive Vector** (`CognitivePlanner`) represents the system's intent. It observes the current state and a `Goal`, then generates a proposed `ActionVector` to achieve that goal.
2.  The **Ethical Matrix** (`ProjectFailsafe`) acts as a guardian. It validates the proposed action against a `ConstitutionalKnowledgeBase` containing immutable safety rules.
3.  The action is only executed by the **Physical System** (`Robot`) if it is deemed safe by the Ethical Matrix.

This architecture ensures that the system's actions are both goal-oriented and provably safe.

## Project Structure

The project is organized into the following directories and files:

- **`main.py`**: The main entry point for the simulation. It initializes all components, sets a goal, and runs a step-by-step simulation demonstrating the core feedback loop.

- **`src/`**: Contains the core source code.
  - **`core/qvc.py`**: Defines the fundamental data structures: `Vector3`, `SystemState`, `ActionVector`, and `Goal`.
  - **`physical/robot.py`**: Contains the `Robot` class, a simple simulation of a physical agent.
  - **`cognitive/planner.py`**: Implements the `CognitivePlanner`, which generates actions to move the robot toward a goal.
  - **`ethical/`**: Implements the Ethical Matrix.
    - **`constitution.py`**: Defines the `ConstitutionalKnowledgeBase` and safety rules (e.g., `MaxVelocityRule`, `ForbiddenZoneRule`).
    - **`failsafe.py`**: Implements `ProjectFailsafe`, the core validation engine.
  - **`creative/`**: (Placeholder) For future generative problem-solving modules.

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

The script runs a goal-oriented simulation where a robot must navigate to a target destination that lies on the other side of a forbidden zone. The output demonstrates:

- **Goal-Oriented Planning**: The `CognitivePlanner` continuously generates actions to move the robot towards the goal.
- **Safe Execution**: In the initial steps, the actions are deemed safe by `ProjectFailsafe` and are executed by the robot, which moves closer to the goal.
- **Ethical Intervention**: As the robot approaches the forbidden zone, the `CognitivePlanner` proposes an action that would cross the boundary. `ProjectFailsafe` identifies this violation, validates the action as **UNSAFE**, and aborts it.
- **System Halts**: The robot stops moving, demonstrating that the safety constraints of the Ethical Matrix override the goal-driven intent of the Cognitive Vector.