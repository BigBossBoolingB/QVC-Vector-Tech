from src.core.qvc import SystemState, Vector3
from src.ethical.constitution import ConstitutionalKnowledgeBase, MaxVelocityRule, ForbiddenZoneRule
from src.ethical.failsafe import ProjectFailsafe
from src.physical.robot import Robot

def run_simulation():
    """
    Runs the main simulation to demonstrate the Ethical Matrix and Project Failsafe.
    """
    print("--- Initializing Chronos Prototype Simulation ---")

    # 1. Define the Constitution (The Ethical Rules)
    constitution = ConstitutionalKnowledgeBase(rules=[
        MaxVelocityRule(max_velocity=1.5),
        ForbiddenZoneRule(
            min_corner=Vector3(x=5.0, y=5.0, z=0.0),
            max_corner=Vector3(x=10.0, y=10.0, z=5.0)
        )
    ])
    print(f"Constitution loaded with {len(constitution.rules)} rules.")

    # 2. Initialize Project Failsafe with the constitution
    failsafe = ProjectFailsafe(constitution=constitution)
    print("Project Failsafe is active.")

    # 3. Initialize the Robot (The Physical System)
    initial_state = SystemState(
        position=Vector3(x=0.0, y=0.0, z=0.0),
        velocity=Vector3(x=0.0, y=0.0, z=0.0)
    )
    robot = Robot(initial_state=initial_state)

    # --- SCENARIO 1: A SAFE ACTION ---
    print("\n--- SCENARIO 1: Proposing a SAFE action ---")
    safe_action = robot.propose_action(target_velocity=Vector3(x=1.0, y=0.5, z=0.0))

    # The Ethical Matrix validates the action
    is_safe = failsafe.validate_action(robot.state, safe_action)
    print(f"Failsafe validation result: {'SAFE' if is_safe else 'UNSAFE'}")

    if is_safe:
        robot.update_state(safe_action)
    else:
        print("Robot action aborted.")
    print(f"Final robot state: {robot.state}")

    # --- SCENARIO 2: AN UNSAFE ACTION (TOO FAST) ---
    print("\n--- SCENARIO 2: Proposing an UNSAFE action (violates max velocity) ---")
    unsafe_action_fast = robot.propose_action(target_velocity=Vector3(x=2.0, y=1.0, z=0.0))

    is_safe = failsafe.validate_action(robot.state, unsafe_action_fast)
    print(f"Failsafe validation result: {'SAFE' if is_safe else 'UNSAFE'}")

    if is_safe:
        robot.update_state(unsafe_action_fast)
    else:
        print("Robot action aborted.")
    print(f"Final robot state: {robot.state}")


    # --- SCENARIO 3: AN UNSAFE ACTION (ENTERING FORBIDDEN ZONE) ---
    print("\n--- SCENARIO 3: Proposing an UNSAFE action (enters forbidden zone) ---")
    # This action has a safe velocity (magnitude ~1.486 < 1.5) but would move the robot
    # from its current position of (1.0, 0.5, 0.0) to (6.0, 6.0, 0.0) in 5 time steps,
    # which is inside the forbidden zone [5:10, 5:10, 0:5].
    unsafe_action_zone = robot.propose_action(target_velocity=Vector3(x=1.0, y=1.1, z=0.0))

    # We check the action over a longer time horizon (5 seconds) to see the violation.
    is_safe = failsafe.validate_action(robot.state, unsafe_action_zone, dt=5.0)
    print(f"Failsafe validation result (predicting 5.0s ahead): {'SAFE' if is_safe else 'UNSAFE'}")

    if is_safe:
        # This block should not be executed.
        print("ERROR: Unsafe action was approved.")
        robot.update_state(unsafe_action_zone)
    else:
        print("Robot action correctly aborted by Failsafe.")
    print(f"Final robot state (unchanged): {robot.state}")


if __name__ == "__main__":
    run_simulation()