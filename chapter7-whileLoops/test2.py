from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
import random
count=0
while count<=5:
    x=random.randrange(-127,128)
    y=random.randrange(0,64)
    z=random.randrange(-127,128)
    mc.postToChat("x:{} y:{} z:{}".format(x,y,z))
    mc.player.setPos(x,y,z)
    count+=1
    time.sleep(3)