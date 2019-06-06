from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time


height=[100,0]
count=0
while count<60:
    x,y,z=mc.player.getPos()
    if y<height[0]:
        height[0]=y
    elif y>height[1]:
        height[1]=y
    count+=1
    time.sleep(1)
mc.postToChat("lowest :"+str(height[0]))
mc.postToChat("highest :"+str(height[1]))












