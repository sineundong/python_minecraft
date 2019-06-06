from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z=mc.player.getPos()
mc.postToChat(x)
mc.postToChat(y)
mc.postToChat(z)
time.sleep(2)
mc.postToChat("hi everyone")
time.sleep(2)
mc.postToChat("x:{}y:{}z:{}".format(x,y,z))

firstname = "eundong"
lastname = "shin"
time.sleep(2)
mc.postToChat(firstname +" "+ lastname)

