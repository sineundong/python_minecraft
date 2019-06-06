from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x1,y1,z1=mc.player.getPos()
time.sleep(10)

x2,y2,z2=mc.player.getPos()
aa = abs(x1-x2)
bb= abs(y1-y2)
cc=abs(z1-z2)
mc.postToChat("x diff : {}y diff :{}z diff :{}".format(aa,bb,cc))
