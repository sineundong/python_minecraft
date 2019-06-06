from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
count=0
sumnum=0
while count<=100:
    if count%2==0:
        mc.postToChat(count)
        sumnum+=count
    count+=1
    time.sleep(0.1)
mc.postToChat("finish")   
mc.postToChat(5050-sumnum)
    