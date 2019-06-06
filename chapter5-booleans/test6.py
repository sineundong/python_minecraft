from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()
yee = mc.getHeight(x,z)

ground=1

if yee >= ground:
    mc.postToChat("in air")
else:
    mc.postToChat("not in air")