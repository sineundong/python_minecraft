from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
blocktype=103
x+=5
y-=1
mc.setBlock(x,y,z,blocktype)
time.sleep(2)
front=2
mc.setBlock(x+front,y,z+front,blocktype)

