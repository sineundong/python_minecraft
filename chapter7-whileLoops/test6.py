from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
while True:
    x,y,z=mc.player.getPos()
    blocktype=38
    mc.setBlock(x,y,z,blocktype)
    time.sleep(0.2)
    