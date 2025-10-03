from src.core.qvc import SystemState, Vector3, Goal
from src.ethical.constitution import ConstitutionalKnowledgeBase, MaxVelocityRule, ForbiddenZoneRule
from src.ethical.failsafe import ProjectFailsafe
from src.physical.robot import Robot
from src.cognitive.planner import CognitivePlanner

def run_simulation_step(planner: CognitivePlanner, robot: Robot, goal: Goal, failsafe: ProjectFailsafe):
    """
    Runs a single step of the goal-oriented simulation.
    """
    print(f"\n--- Robot at {robot.state.position} ---")
    # 1. Cognitive Vector proposes an action based on the goal
    action = planner.generate_action(robot.state, goal)

    # 2. Ethical Matrix validates the action
    is_safe = failsafe.validate_action(robot.state, action)
    print(f"FAILSAFE validation result: {'SAFE' if is_safe else 'UNSAFE'}")

    # 3. Physical system executes the action ONLY if it's safe
    if is_safe:
        robot.update_state(action)
    else:
        print("ACTION ABORTED by Failsafe. Robot holds position.")
        # In a real system, the planner would be notified of the failure
        # and would need to generate a new plan. For this demo, we just stop.

    return is_safe

def main():
    """
    Runs the main simulation to demonstrate the interaction between the
    Cognitive Planner and the Ethical Matrix.
    """
    print("--- Initializing Chronos Prototype: Cognitive & Ethical Integration ---")

    # 1. Define the Constitution (The Ethical Rules)
    # The Failsafe will reject any action with velocity > 1.0
    # or any action that leads into the zone [4:8, 4:8, 0:5]
    constitution = ConstitutionalKnowledgeBase(rules=[
        MaxVelocityRule(max_velocity=1.0),
        ForbiddenZoneRule(
            min_corner=Vector3(x=4.0, y=4.0, z=0.0),
            max_corner=Vector3(x=8.0, y=8.0, z=5.0)
        )
    ])
    failsafe = ProjectFailsafe(constitution=constitution)

    # 2. Initialize the Cognitive Planner
    # The planner's speed is set to 0.9, which is compliant with the
    # Failsafe's max_velocity rule of 1.0. This allows the robot to move
    # until it encounters the forbidden zone.
    planner = CognitivePlanner(max_speed=0.9)

    # 3. Initialize the Robot
    robot = Robot(initial_state=SystemState(position=Vector3(x=0, y=0, z=0), velocity=Vector3()))

    # 4. Define a Goal
    # This goal is on the other side of the forbidden zone.
    goal = Goal(target_position=Vector3(x=10, y=10, z=0))
    print(f"Goal set to: {goal.target_position}")

    # --- Run Simulation ---
    # The simulation will run for a few steps. The planner will try to move
    # directly towards the goal, but the Failsafe will block it as it
    # approaches the forbidden zone.
    for i in range(10):
        print(f"\n--- Simulation Step {i+1} ---")
        is_safe = run_simulation_step(planner, robot, goal, failsafe)
        if not is_safe:
            print("\nSimulation halted due to Failsafe intervention.")
            break

if __name__ == "__main__":
    main()