from mcpi.minecraft import Minecraft
from minecraftstuff import MinecraftDrawing
mc=Minecraft.create()

blocktype=103

x,y,z=mc.player.getPos()

mcd=MinecraftDrawing(mc)
mcd.drawCircle( x+10, y, z, 20,blocktype)