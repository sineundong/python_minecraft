from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=10
y=50
z=35
time.sleep(1)
mc.player.setPos(x,y,z)
#x=x+5   # x+=5
x+=5
blocktype=103
mc.setBlock(x,y,z,blocktype)
time.sleep(2)
y=10
y+=1
blocktype=64
mc.setBlock(x,y,z,blocktype)

