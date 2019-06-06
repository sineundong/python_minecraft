from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftTurtle

mc = Minecraft.create()
pos = mc.player.getTilePos()

# create minecraft turtle
steve = MinecraftTurtle(mc, pos)

# draw a pentagon
steve.forward(5)
steve.right(72)
steve.forward(5)
steve.right(72)
steve.forward(5)
steve.right(72)
steve.forward(5)
steve.right(72)
steve.forward(5)