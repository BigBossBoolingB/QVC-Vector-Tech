import json
from dataclasses import dataclass, asdict
from typing import List
from src.core.qvc import SystemState, ActionVector

@dataclass
class MemoryRecord:
    """
    An immutable record of a single time step in the simulation.
    """
    step: int
    state: SystemState
    proposed_action: ActionVector
    is_safe: bool

    def to_dict(self):
        """Converts the record to a dictionary for serialization."""
        return asdict(self)

class SimulationHistory:
    """
    Manages a chronological log of MemoryRecords and handles saving them.
    """
    def __init__(self):
        self.records: List[MemoryRecord] = []
        print("SimulationHistory initialized.")

    def add_record(self, record: MemoryRecord):
        """Adds a new record to the history."""
        self.records.append(record)

    def save_to_file(self, filepath: str = "simulation_log.json"):
        """
        Saves the entire simulation history to a JSON file.
        """
        history_as_dict = [record.to_dict() for record in self.records]
        with open(filepath, 'w') as f:
            json.dump(history_as_dict, f, indent=4)
        print(f"Simulation history successfully saved to {filepath}")