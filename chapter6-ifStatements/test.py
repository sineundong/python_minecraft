from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block
x,y,z=mc.player.getPos()
front=5
airblock=block.AIR.id
blocktype=block.WOOD.id
for i in range(5):
    print(i)
    time.sleep(1)
    mc.setBlock(x+front,y,z+i,airblock)
    

for i in range(5):
    print(i)
    time.sleep(1)
    mc.setBlock(x+front,y,z+i,blocktype)
    
for i in range(5):
    print(i)
    time.sleep(1)
    mc.setBlock(x+front,y+i,z+i,blocktype)
    
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
    mc.setBlock(x+front,y+i,z+i,airblock)
    
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
    mc.setBlock(x+front,y+i,z+i,block.MELON.id)
    