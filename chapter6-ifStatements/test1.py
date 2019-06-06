from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block

a=input()
if a=="yes":
    x,y,z=mc.player.getPos()
    mc.setBlocks(x+5,y,z,x+10,y+5,z+5,block.GLASS.id)
    mc.postToChat("create")

    
    
    
