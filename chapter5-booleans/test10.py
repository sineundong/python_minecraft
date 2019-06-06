from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time
x,y,z=mc.player.getPos()
blocktype=mc.getBlock(x,y-1,z)
intree=(blocktype == block.WOOD.id or blocktype == block.LEAVES.id)
mc.postToChat("tree or leaves:{}".format(intree))