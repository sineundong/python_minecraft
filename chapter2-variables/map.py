import sys
from mcpi.minecraft import Minecraft

from mcpi import block
# import server


mc = Minecraft.create()
mc.setBlocks(-128,0,-128,128,64,128,0)
if(len(sys.argv) > 1):
        bid = int(sys.argv[1])
else:
        bid = block.SANDSTONE.id

if bid < 0 or bid > 108:
        bid = block.SANDSTONE.id

mc.setBlocks(-128,0,-128,128,-64,128,bid)
