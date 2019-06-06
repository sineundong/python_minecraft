from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import time
import random

x,y,z=mc.player.getPos()
while True:
    a=random.uniform(-0.2,0.2)
    print(a)
    x+=random.uniform(-0.2,0.2)
    b=random.uniform(-0.2,0.2)
    print(b)
    y=mc.getHeight(x,z)
    
    mc.player.setPos(x,y,z)
    time.sleep(0.1)

    

