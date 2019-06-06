from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftDrawing
#pip install minecraftstuff
mc = Minecraft.create()

mcdraw = MinecraftDrawing(mc)

# draw a diagonal line
mcdraw.drawLine(0,0,0,10,10,10,block.STONE.id)