from src.core.qvc import SystemState, ActionVector, Vector3
from src.ethical.constitution import ConstitutionalKnowledgeBase, ForbiddenZoneRule

class ProjectFailsafe:
    """
    The core of the Ethical Matrix. Validates actions against the constitution.
    """
    def __init__(self, constitution: ConstitutionalKnowledgeBase):
        self.constitution = constitution

    def validate_action(self, state: SystemState, action: ActionVector, dt: float = 1.0) -> bool:
        """
        Validates a proposed action against all rules in the constitution.

        Args:
            state: The current state of the system.
            action: The proposed action to be validated.
            dt: The time step for prediction.

        Returns:
            True if the action is safe, False otherwise.
        """
        # 1. Check against Max Velocity Rule
        max_velocity_rule = self.constitution.get_max_velocity_rule()
        if max_velocity_rule:
            if action.target_velocity.magnitude() > max_velocity_rule.max_velocity:
                print(f"FAILSAFE: Action violates Max Velocity rule ({action.target_velocity.magnitude()} > {max_velocity_rule.max_velocity})")
                return False

        # 2. Check against Forbidden Zone Rules
        forbidden_zones = self.constitution.get_forbidden_zone_rules()
        if forbidden_zones:
            # Predict the next position
            predicted_position_arr = state.position.to_array() + action.target_velocity.to_array() * dt
            predicted_position = Vector3.from_array(predicted_position_arr)

            for zone in forbidden_zones:
                if self._is_inside_zone(predicted_position, zone):
                    print(f"FAILSAFE: Action leads to entering a forbidden zone at {predicted_position}")
                    return False

        # If all checks pass, the action is safe
        return True

    def _is_inside_zone(self, position: Vector3, zone: ForbiddenZoneRule) -> bool:
        """Checks if a position is inside a forbidden zone."""
        is_inside_x = zone.min_corner.x <= position.x <= zone.max_corner.x
        is_inside_y = zone.min_corner.y <= position.y <= zone.max_corner.y
        is_inside_z = zone.min_corner.z <= position.z <= zone.max_corner.z
        return is_inside_x and is_inside_y and is_inside_z