from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block

def dia():
    
    return block.DIAMOND_BLOCK.id

def tower(x,y,z):
    
    width=10
    height=10
    length=10
    mc.setBlocks(x,y,z,x+width,y+height,z+length,dia())
x,y,z=mc.player.getPos()


for i in range(0,100,10):
    tower(x+15,y,z+i)
    
time.sleep(2)
 
for i in range(0,100,10): 
    tower(x+15,y+10,z+i)