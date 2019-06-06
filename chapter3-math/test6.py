from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

#===============================================================================
# x=10
# y=1
# z=10
# mc.player.setPos(x,y,z)
#===============================================================================

x,y,z=mc.player.getPos()
x+=5
blocktype=103
mc.setBlock(x,y,z,blocktype)
y+=1
mc.setBlock(x,y,z,blocktype)
time.sleep(1)
y+=1
mc.setBlock(x,y,z,blocktype)
time.sleep(1)
y+=1
mc.setBlock(x,y,z,blocktype)
