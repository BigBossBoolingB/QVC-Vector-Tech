from src.core.qvc import SystemState, ActionVector, Vector3

class Robot:
    """
    A simulated robotic arm representing a physical system.
    """
    def __init__(self, initial_state: SystemState):
        self.state = initial_state
        print(f"Robot initialized at position {self.state.position} with velocity {self.state.velocity}")

    def update_state(self, action: ActionVector, dt: float = 1.0):
        """
        Updates the robot's state based on a validated action.
        This simulates the physical execution of the command.
        """
        # Update velocity first
        self.state.velocity = action.target_velocity

        # Update position based on the new velocity
        new_position_arr = self.state.position.to_array() + self.state.velocity.to_array() * dt
        self.state.position = Vector3.from_array(new_position_arr)

        print(f"Robot moved to {self.state.position} with velocity {self.state.velocity}")
