from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x=20
y=40
z=17
time.sleep(1)
mc.player.setPos(x,y,z)
x=x+5
y=1
time.sleep(3)
mc.player.setPos(x,y,z)
z=z+5
time.sleep(1)
mc.player.setPos(x,y,z)



