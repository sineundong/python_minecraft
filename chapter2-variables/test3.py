from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x=20
y=10
z=15
mc.player.setPos(x,y,z)
mc.postToChat("misson 1 clear")

time.sleep(2)
x=50
y=40
z=30
mc.player.setPos(x,y,z)
time.sleep(1)
mc.postToChat("misson 2 clear")
