from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
position=mc.player.getPos()
x=position.x
y=position.y
z=position.z

msg="x:{}y:{}z:{} ".format(x,y,z)
mc.postToChat(msg)


#printf(" %d" ,%d)
#print(" %d" %(d))

