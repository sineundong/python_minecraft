from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
#position=mc.player.getPos()

x,y,z=mc.player.getPos() # tuple 
x+=5
blocktype=17
mc.setBlock(x,y,z,blocktype)
z+=1
time.sleep(1)
mc.setBlock(x,y,z,blocktype)
y+=10
x+=5
z+=5
mc.player.setPos(x,y,z)

