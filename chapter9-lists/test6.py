from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block
x,y,z=mc.player.getPos()
blocks=[i for i in range(1,10)]
for i in range(len(blocks)):
    if i==10 or i==block.WATER_STATIONARY.id or i==block.WATER.id or i==9 or i==7 or i==8:
        
        mc.setBlock(x+5,y+10,z,block.AIR.id)
    else:
        mc.setBlock(x+5,y+i-1,z,blocks[i])
    


print(block.LAVA.id)
