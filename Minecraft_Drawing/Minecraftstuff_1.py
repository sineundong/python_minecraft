from minecraftstuff import MinecraftDrawing
from mcpi.minecraft import Minecraft
from mcpi import block
#https://minecraft-stuff.readthedocs.io/en/latest/minecraftdrawing.html
## pip install minecraftstuff
#Connect to minecraft
mc = Minecraft.create()
# get the players position
pos = mc.player.getTilePos()

#Using the Minecraft Drawing API
mcdrawing = MinecraftDrawing(mc)


# draw a circle with a radius of 10 blocks
#mcdrawing.drawCircle(pos.x, pos.y + 15, pos.z, 10, block.WOOD.id)
mcdrawing.drawCircle(pos.x+10, pos.y+5, pos.z+10, 5, block.WOOD.id)
