from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block
air=block.AIR.id
while True:
    
    x,y,z=mc.player.getPos()
    below=mc.getBlock(x,y-1,z)
    if below==block.ICE.id:
        mc.setBlock(x,y-1,z,block.GLASS.id)
       
    else:
        print("nono")