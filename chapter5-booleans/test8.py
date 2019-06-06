from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
import math
x1,y1,z1=mc.player.getPos()
time.sleep(5)
x2,y2,z2=mc.player.getPos()
a=math.sqrt((x2-x1)**2+(z2-z1)**2)
mc.postToChat(a)

# c**2=a**2+b**2