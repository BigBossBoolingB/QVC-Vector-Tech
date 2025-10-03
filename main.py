from src.core.qvc import SystemState, Vector3, Goal
from src.ethical.constitution import ConstitutionalKnowledgeBase, MaxVelocityRule, ForbiddenZoneRule
from src.ethical.failsafe import ProjectFailsafe
from src.physical.robot import Robot
from src.cognitive.planner import CognitivePlanner
from src.simulation import Simulation

def main():
    """
    Configures and runs the simulation using the new modular framework.
    This script is now the main entry point and configuration hub.
    """
    print("--- Configuring Chronos Simulation Framework ---")

    # 1. Configure the Ethical Matrix
    constitution = ConstitutionalKnowledgeBase(rules=[
        MaxVelocityRule(max_velocity=1.0),
        ForbiddenZoneRule(
            min_corner=Vector3(x=4.0, y=4.0, z=0.0),
            max_corner=Vector3(x=8.0, y=8.0, z=5.0)
        )
    ])
    failsafe = ProjectFailsafe(constitution=constitution)

    # 2. Configure the Cognitive Vector (The Planner)
    planner = CognitivePlanner(max_speed=0.9)

    # 3. Configure the Physical System (The Robot)
    robot = Robot(initial_state=SystemState(position=Vector3(x=0, y=0, z=0), velocity=Vector3()))

    # 4. Configure the Goal
    goal = Goal(target_position=Vector3(x=10, y=10, z=0))

    # 5. Instantiate the Simulation Framework
    simulation = Simulation(robot=robot, planner=planner, failsafe=failsafe, goal=goal)

    # 6. Run the Simulation and get the history
    history = simulation.run(max_steps=10)

    # 7. Save the results
    history.save_to_file("simulation_log.json")

    print("\n--- Main script finished ---")

if __name__ == "__main__":
    main()