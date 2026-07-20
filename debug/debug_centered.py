import numpy as np
from SimMain import RectangleLightSail

sail = RectangleLightSail(1.0, 1.0, 10, 0.0, 0.0)
sail.positionOffset = np.array([0.0, 0.0, 0.0])
sail.velocity = np.zeros(3)
sail.thetaX = 0.0
sail.thetaY = 0.0
sail.angularVelocity = np.zeros(3)

force, torque = sail.compute()
print('force', force)
print('torque', torque)

# One step update
sail.update(0.01, 0.0)
print('positionOffset after one step', sail.positionOffset)
print('velocity after one step', sail.velocity)

# Long-term drift test
sail.positionOffset = np.array([0.0, 0.0, 0.0])
sail.velocity = np.zeros(3)
sail.angularVelocity = np.zeros(3)

steps = 500
positions = []
forces = []
for i in range(steps):
    sail.update(0.01, i*0.01)
    positions.append(sail.positionOffset.copy())
    forces.append(sail.Force.copy())

positions = np.array(positions)
forces = np.array(forces)
print('\nFinal position after long run:', positions[-1])
print('Drift XY:', positions[-1][:2])
print('Max force XY magnitude:', np.max(np.linalg.norm(forces[:,:2], axis=1)))
print('Min/max force X:', forces[:,0].min(), forces[:,0].max())
print('Min/max force Y:', forces[:,1].min(), forces[:,1].max())
