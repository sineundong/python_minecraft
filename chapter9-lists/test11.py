from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time
x,y,z=mc.player.getPos()
blocks=[57,41,22,42,103,54,3,2,45]

#block=random.choice(blocks)
count=0
#c.setBlock(x+5,y,z,block)
while True:
    count+=1  
    for i in range(0,30,1):  
        for j in range(10):
            
            block=random.choice(blocks)
            print(block)
            mc.setBlock(x+5+count,y+j,z+i,block)
            
            time.sleep(0.8)
    if count==2:    
        break
print("hahahaahhaaahahaaaahah finish")