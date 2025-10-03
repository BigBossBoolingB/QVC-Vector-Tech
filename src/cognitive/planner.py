import numpy as np
from src.core.qvc import SystemState, ActionVector, Goal, Vector3

class CognitivePlanner:
    """
    A simple planner representing the Cognitive Vector.
    Its job is to generate an action to move the system towards a goal.
    """
    def __init__(self, max_speed: float = 1.0):
        self.max_speed = max_speed
        print(f"Cognitive Planner initialized with max_speed: {self.max_speed}")

    def generate_action(self, state: SystemState, goal: Goal) -> ActionVector:
        """
        Generates an action to move from the current state towards the goal.
        """
        direction_vector = goal.target_position.to_array() - state.position.to_array()
        distance = np.linalg.norm(direction_vector)

        if distance < 0.1:  # Close enough to the goal
            # Propose stopping
            target_velocity = Vector3(x=0.0, y=0.0, z=0.0)
            print("COGNITIVE: Goal reached. Proposing to stop.")
        else:
            # Propose moving towards the goal at a normalized speed
            # The speed is capped by self.max_speed
            normalized_direction = direction_vector / distance
            target_velocity_arr = normalized_direction * self.max_speed
            target_velocity = Vector3.from_array(target_velocity_arr)
            print(f"COGNITIVE: Proposing action to move towards {goal.target_position} with velocity {target_velocity}")

        return ActionVector(target_velocity=target_velocity)