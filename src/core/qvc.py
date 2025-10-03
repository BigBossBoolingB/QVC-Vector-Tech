from dataclasses import dataclass
import numpy as np

@dataclass
class Vector3:
    """A simple dataclass to represent a 3D vector."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def to_array(self) -> np.ndarray:
        return np.array([self.x, self.y, self.z])

    @staticmethod
    def from_array(arr: np.ndarray):
        if arr.shape != (3,):
            raise ValueError("Input array must have shape (3,)")
        return Vector3(x=arr[0], y=arr[1], z=arr[2])

    def magnitude(self) -> float:
        return np.linalg.norm(self.to_array())

@dataclass
class SystemState:
    """Represents the current state of a physical system."""
    position: Vector3
    velocity: Vector3

@dataclass
class ActionVector:
    """Represents a proposed action to be applied to a physical system."""
    # For a simple robotic arm, this could be a target velocity vector.
    target_velocity: Vector3
    # Could also include force, torque, etc. in a more complex model.
    force: float = 0.0

@dataclass
class Goal:
    """Represents a target destination for the system."""
    target_position: Vector3