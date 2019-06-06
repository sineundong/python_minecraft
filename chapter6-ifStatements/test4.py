from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block
x,y,z=mc.player.getPos()

front=5
width=10
length=5
height=5
blocktype=block.WOOL.id
mc.setBlocks(x+front,y,z,x+front+width,y+height,z+length,blocktype)
time.sleep(1)
mc.setBlocks(x+front+1,y+1,z,x+front+width-1,y+height-1,z+1,block.GLASS.id)

