from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time
x,y,z=mc.player.getPos()
blocktype=block.STONE.id
front=5
width=5
depth=5
height=5
mc.setBlocks(x+front,y,z+front,x+front+width*2,y,z+front+depth*2,blocktype)