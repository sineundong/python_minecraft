from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time


def treemake(x,y,z):
    wood=17
    leaves=18
    # trunck
    mc.setBlocks(x,y,z,x,y+5,z,wood)
    # leaves
    mc.setBlocks(x-2,y+6,z-2,x+2,y+6,z+2,leaves)
    # leaves 2
    mc.setBlocks(x-1,y+7,z-1,x+1,y+7,z+1,leaves)
    
x,y,z=mc.player.getPos()
# treemake(x+10,y,z)
# treemake(x+15,y,z)
for i in range(1,11):
    treemake(x+10*i,y,z+10*i)

    time.sleep(1)
for j in range(11,0,-1):
    treemake(x+10*j,y,z)    
    time.sleep(1)