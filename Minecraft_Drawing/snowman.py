from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
front=20
#y+=1
blocktype=block.SNOW_BLOCK.id

def snowman(x,y,z):
    time.sleep(3)
    mc.setBlocks(x+front,y,z,x+front+6,y+6,z+6,blocktype)
    time.sleep(1)
    mc.setBlocks(x+front+1,y+7,z+1,x+front+5,y+11,z+5,blocktype)
    time.sleep(1)
    mc.setBlock(x+front,y+5,z+3,block.DIAMOND_BLOCK.id)
    time.sleep(1)
    mc.setBlock(x+front,y+3,z+3,block.DIAMOND_BLOCK.id)
    time.sleep(1)
    mc.setBlock(x+front,y+1,z+3,block.DIAMOND_BLOCK.id)
    time.sleep(1)
    mc.setBlock(x+front+1,y+7,z+3,35,15)
    mc.setBlock(x+front+1,y+8,z+2,35,15)
    mc.setBlock(x+front+1,y+8,z+4,35,15)
    time.sleep(1)
    mc.setBlock(x+front+1,y+10,z+2,35,15)
    mc.setBlock(x+front+1,y+10,z+4,35,15)
    time.sleep(1)
    mc.setBlocks(x+front+1,y+9,z+3,x+front,y+9,z+3,35,14)
    time.sleep(1)
    mc.setBlocks(x+front+1,y+13,z+1,x+front+5,y+15,z+5,block.IRON_BLOCK.id)
    time.sleep(1)
    mc.setBlocks(x+front,y+12,z,x+front+6,y+12,z+6,block.IRON_BLOCK.id)
    
snowman(x+5,y,z)
snowman(x+5,y,z+10)