from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
blocks=[i for i  in range(10)] 

barblock=22
count=0
while count<=len(blocks):
    for i in range(10):
        mc.setBlock(x+5,y+i,z,blocks[i])
        
    time.sleep(1)    
    del blocks[9]
    count+=1
    blocks.insert(0,barblock)
    time.sleep(2)