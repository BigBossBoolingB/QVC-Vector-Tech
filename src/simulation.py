import copy
from src.core.qvc import Goal
from src.physical.robot import Robot
from src.cognitive.planner import CognitivePlanner
from src.ethical.failsafe import ProjectFailsafe
from src.core.memory import SimulationHistory, MemoryRecord

class Simulation:
    """
    Encapsulates the entire simulation loop, making the framework modular and reusable.
    """
    def __init__(self, robot: Robot, planner: CognitivePlanner, failsafe: ProjectFailsafe, goal: Goal):
        self.robot = robot
        self.planner = planner
        self.failsafe = failsafe
        self.goal = goal
        self.history = SimulationHistory()
        print("Simulation framework initialized.")

    def run(self, max_steps: int = 20) -> SimulationHistory:
        """
        Runs the simulation for a given number of steps.

        Args:
            max_steps: The maximum number of steps to run the simulation for.

        Returns:
            The simulation history log.
        """
        print(f"\n--- Starting Simulation (max_steps={max_steps}) ---")
        print(f"Goal set to: {self.goal.target_position}")

        for i in range(max_steps):
            current_state = self.robot.state

            # 1. Cognitive Vector proposes an action
            action = self.planner.generate_action(current_state, self.goal)

            # 2. Ethical Matrix validates the action
            is_safe = self.failsafe.validate_action(current_state, action)

            # 3. Record the memory of this step (with a deepcopy to prevent reference bugs)
            record = MemoryRecord(step=i, state=copy.deepcopy(current_state), proposed_action=action, is_safe=is_safe)
            self.history.add_record(record)

            print(f"Step {i}: Failsafe validation: {'SAFE' if is_safe else 'UNSAFE'}")

            # 4. Execute action if safe, otherwise halt
            if is_safe:
                self.robot.update_state(action)
            else:
                print("HALT: Action aborted by Failsafe. Ending simulation.")
                break

        print("\n--- Simulation Finished ---")
        return self.history