from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block
x,y,z=mc.player.getPos()
#blocktype=mc.getBlock(x,y,z)
blocktype=block.ICE.id
while True:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y-1,z,blocktype)

