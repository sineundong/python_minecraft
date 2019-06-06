from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block
count=0
while count<=30:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y,z,block.GRASS.id)
    count+=1
    time.sleep(1)
    