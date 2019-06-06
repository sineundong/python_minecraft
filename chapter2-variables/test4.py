from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x=5.5
y=40.6
z=44.7
mc.player.setPos(x,y,z)
mc.postToChat("float values:")


