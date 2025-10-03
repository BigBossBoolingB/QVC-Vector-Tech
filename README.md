# Chronos Framework: A Foundation for Safe AI/ML/Robotics

This project provides a reusable and extensible software framework for building and simulating safe autonomous systems. It is designed as a foundational starting point for AI, Machine Learning, and Robotics projects, with a core focus on integrating an **Ethical Matrix** to govern the actions of an intelligent agent.

## Core Architecture

The framework is built on a modular, component-based architecture that separates concerns, making it highly configurable.

1.  **Cognitive Vector (`CognitivePlanner`)**: The "mind" of the agent. This component is responsible for generating goal-oriented actions based on the system's current state.
2.  **Ethical Matrix (`ProjectFailsafe`)**: The "conscience" of the agent. It validates every proposed action against a set of immutable safety rules defined in a `ConstitutionalKnowledgeBase`.
3.  **Physical System (`Robot`)**: A simulation of the agent's body or the system it controls.
4.  **Simulation Engine (`Simulation`)**: The core of the framework. It encapsulates the main simulation loop, manages the interaction between the other components, and records the outcome of every step.
5.  **Memory System (`SimulationHistory`)**: A persistent logging system that records every state, proposed action, and safety outcome into a `simulation_log.json` file. This "memory vector" log is essential for debugging, analysis, and as a dataset for future machine learning tasks.

## Project Structure

- **`main.py`**: The main entry point. This script is used for configuring and launching the simulation. You can easily swap out different planners, robots, or rule sets here.
- **`simulation_log.json`**: The output file containing the complete history of the last simulation run.

- **`src/`**: Contains the core framework source code.
  - **`simulation.py`**: Houses the main `Simulation` class.
  - **`core/`**: Defines the foundational data structures.
    - **`qvc.py`**: `Vector3`, `SystemState`, `ActionVector`, `Goal`.
    - **`memory.py`**: `MemoryRecord` and `SimulationHistory` for logging.
  - **`physical/robot.py`**: A sample `Robot` implementation.
  - **`cognitive/planner.py`**: A sample `CognitivePlanner` implementation.
  - **`ethical/`**: The Ethical Matrix components.
    - **`constitution.py`**: Defines the safety rule structures.
    - **`failsafe.py`**: The core `ProjectFailsafe` validation engine.
  - **`creative/`**: (Placeholder) For future generative problem-solving modules.

## How to Run the Simulation

1.  **Install Dependencies**: The project requires `numpy`.
    ```bash
    pip install numpy
    ```

2.  **Configure and Run**: Modify `main.py` to set up your desired scenario (e.g., change the robot's starting position, the goal, or the safety rules). Then, execute the script from the root directory.
    ```bash
    python3 main.py
    ```

3.  **Check the Output**: After the simulation runs, a `simulation_log.json` file will be created in the root directory. This file contains a detailed, step-by-step log of the simulation, perfect for analysis.

## Use as a Foundation

This framework is designed to be the starting point for your own projects:
- **Build a new AI**: Create a more advanced planner in `src/cognitive/` that uses a machine learning model.
- **Simulate a new robot**: Create a new class in `src/physical/` with different physics or capabilities.
- **Define new ethics**: Add new, more complex rules to the `ConstitutionalKnowledgeBase`.
- **Train a model**: Use the `simulation_log.json` output as a training dataset to teach a new planner how to avoid unsafe actions.