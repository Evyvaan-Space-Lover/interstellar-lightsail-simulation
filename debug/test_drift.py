import numpy as np
from SimMain import RectangleLightSail

# Create a centered, untilted rectangular sail
sail = RectangleLightSail(1.0, 1.0, 10, 1.0, 0.01)
sail.positionOffset = np.array([0.0, 0.0, 0.0])
sail.velocity = np.array([0.0, 0.0, 0.0])
sail.thetaX = 0.0
sail.thetaY = 0.0
sail.angularVelocity = np.array([0.0, 0.0, 0.0])

# Run a longer simulation
dt = 0.01
steps = 500

positions = []
print("Running simulation... step: ", end='', flush=True)
for step in range(steps):
    if step % 50 == 0:
        print(f"{step} ", end='', flush=True)
    sail.update(dt, dt * step)
    positions.append(sail.positionOffset.copy())
print()

positions = np.array(positions)

print("Initial position:", positions[0])
print("Final position:", positions[-1])
print("Drift (final - initial):", positions[-1] - positions[0])
print("Max drift magnitude:", np.max(np.linalg.norm(positions - positions[0], axis=1)))

# Print a few intermediate positions to see drift evolution
print("\nDrift evolution:")
for i in [0, 50, 100, 250, 499]:
    drift_i = positions[i] - positions[0]
    print(f"Step {i:4d}: position = {positions[i]}, drift = {drift_i}")

