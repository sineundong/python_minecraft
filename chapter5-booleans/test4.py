from mcpi.minecraft import Minecraft
import time
from mcpi import block
mc=Minecraft.create()
x,y,z=mc.player.getPos()
fromt=5
blocktype = block.GOLD_BLOCK.id
mc.setBlock(x+fromt,y,z,blocktype)

blocktype2 = mc.getBlock(x+fromt,y,z)
mc.postToChat(blocktype == blocktype2)

if blocktype!=blocktype2:
    print("same")
else:
    print("different")

# a=2  a==2

# ==  !=  >=   <= 