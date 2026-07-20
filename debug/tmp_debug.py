from SimMain import RectangleLightSail

sail = RectangleLightSail(10, 10, 100, 0, 0, 0.0, 0.0)

F, T = sail.compute()
print('compute force', F)
print('compute torque', T)
print('initial pos', sail.positionOffset.tolist(), 'vel', sail.velocity.tolist())
for step in range(5):
    sail.compute()
    sail.update(0.1, 0.1 * step)
    print('step', step, 'pos', sail.positionOffset.tolist(), 'vel', sail.velocity.tolist(), 'force', sail.Force.tolist())
