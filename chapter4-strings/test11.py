from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
blocktype=int(input(":"))
x,y,z=mc.player.getPos()
mc.setBlock(x+5,y,z,blocktype)
time.sleep(2)
mc.setBlock(x+5,y,z+5,blocktype)
mc.postToChat("mission clear")
