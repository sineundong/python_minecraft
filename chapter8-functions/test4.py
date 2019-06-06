from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time


def melonmake(x,y,z):
    melon=103
    mc.setBlock(x,y,z,melon)
    
x,y,z=mc.player.getPos()
for i in range(1,11):
    melonmake(x+2*i,y,z)
    time.sleep(0.5)
    melonmake(x,y,z+2*i)
    time.sleep(0.5)
    melonmake(x,y+2*i,z)
    time.sleep(0.5)
    melonmake(x+2*i,y+2*i,z+2*i)
    
    
    
    
    
