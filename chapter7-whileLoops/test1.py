from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
count=0
while count<=5:
    print(count)
    mc.postToChat(count)
    if count==3:
        break
    count+=1
    time.sleep(1)
mc.postToChat("finish")


# for 
for i in range(6):
    mc.postToChat(i)
    time.sleep(1)
