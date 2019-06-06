from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block


def melon():
    
   return block.MELON.id 
    
def water():
    
    return block.WATER.id

def wool(): 
    
    return block.WOOL.id

def tnt():
    
    return block.TNT.id

def flower():
    
    return block.FLOWER_YELLOW.id

x,y,z=mc.player.getPos()
#mc.setBlock(x+5,y,z,melon())
#mc.setBlock(x+5,y+1,z,water())
count=0
while True:
    mc.setBlock(x+5,y,z+count,tnt())
    count+=1
    mc.setBlock(x+5,y,z+count,wool())
    count+=1
    mc.setBlock(x+5,y,z+count,melon())
    count+=1
    mc.setBlock(x+5,y,z+count,flower())
    count+=1
    print(count)
    if count>20:
        mc.postToChat("clear")
        break
    time.sleep(0.5)
