from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x,y,z=mc.player.getPos()

try:
    blocktype=int(input(":"))
    mc=setBlock(x+5,y,z,blocktype)
except:
    mc.postToChat("error")