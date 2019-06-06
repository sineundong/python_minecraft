from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
from mcpi import block
x,y,z=mc.player.getPos()
blocktype=mc.getBlock(x,y,z)
underwater=(blocktype == 9)
mc.postToChat("underwater :{}".format(underwater))
# " " +str(underwater)

