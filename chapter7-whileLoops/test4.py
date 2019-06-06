from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
m=""
while m!="exit" :
    m=""
    m=input()
    mc.postToChat(m)
    time.sleep(1)
mc.postToChat("finish")