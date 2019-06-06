from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

a=100000

mc.postToChat(a)
time.sleep(1)
a=200
mc.postToChat(a)
b="today is friday"
mc.postToChat(b)

b="cat and dog"
time.sleep(1)
mc.postToChat(b)

