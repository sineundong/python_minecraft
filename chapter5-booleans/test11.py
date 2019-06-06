from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from mcpi import block
import time
x,y,z=mc.player.getPos()
blocktype=block.MELON.id
mc.setBlock(x+5,y,z,blocktype)


blocktype2=mc.getBlock(x+5,y,z)
melon=(blocktype == blocktype2)
mc.postToChat("I make melon block and get block is :{}".format(melon))