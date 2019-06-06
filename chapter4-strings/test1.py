from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
mc.postToChat("test")

a="test"
b="program"

msg="{0} {1} {0}".format(a,b)
mc.postToChat(msg)



del a
print(a)