import numpy as np
from SimMain import RectangleLightSail
sail=RectangleLightSail(10,10,100,0,0,0.0,0.0)
for t in range(20):
    sail.update(0.1,t*0.1)
    print(sail.positionOffset.tolist(), sail.velocity.tolist())
