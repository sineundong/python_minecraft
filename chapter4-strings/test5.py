from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()



# while True:
blocktype=int(input("input your block number"))
x,y,z= mc.player.getPos()
time.sleep(1)
front=5
mc.setBlock(x+front,y,z,blocktype)

