from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
from mcpi import block
 
 
x,y,z=mc.player.getPos()
airblock = block.AIR.id
#print(block.AIR.id)
blocktype = mc.getBlock(x,y-1,z)
if airblock == blocktype:
    mc.postToChat("in air")
else: 
    mc.postToChat("not in air")

air=blocktype == airblock
#zair =True

if air==True : 
    mc.postToChat("in air")
else:
    mc.postToChat("not in air")