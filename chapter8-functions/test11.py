from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
from mcpi import block

def woolcolor(color):
    blockcolor=0
    if color=="pink":
        blockcolor = 6
    elif color == "black":
        blockcolor=15
    elif color == "red":
        blockcolor=14
    elif color == "grey":
        blockcolor=7
    elif color == "green":
        blockcolor=5
    else:
        blockcolor=4
    return blockcolor

        


while True:
    a=input()
    x,y,z=mc.player.getPos()
    woolblock=block.WOOL.id
    mc.setBlock(x+5,y,z,woolblock,woolcolor(a))