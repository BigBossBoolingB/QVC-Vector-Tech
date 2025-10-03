from dataclasses import dataclass
from src.core.qvc import Vector3

@dataclass
class SafetyRule:
    """Base class for all safety rules."""
    pass

@dataclass
class MaxVelocityRule(SafetyRule):
    """Rule to enforce a maximum velocity."""
    max_velocity: float

@dataclass
class ForbiddenZoneRule(SafetyRule):
    """Rule to define a forbidden zone (as a bounding box)."""
    min_corner: Vector3
    max_corner: Vector3

@dataclass
class ConstitutionalKnowledgeBase:
    """A collection of safety rules that govern the system."""
    rules: list[SafetyRule]

    def get_max_velocity_rule(self) -> MaxVelocityRule | None:
        for rule in self.rules:
            if isinstance(rule, MaxVelocityRule):
                return rule
        return None

    def get_forbidden_zone_rules(self) -> list[ForbiddenZoneRule]:
        return [rule for rule in self.rules if isinstance(rule, ForbiddenZoneRule)]