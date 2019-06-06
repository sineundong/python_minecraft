from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
width=10
height=12
length=13
melon=103
mc.setBlocks(x,y,z,x+width,y+height,z+length,melon)
mc.setBlocks(x+20,y,z+20,x+20+width,y+height,z+20+length,melon)
mc.player.setPos(x+20,y+30,z+20)
