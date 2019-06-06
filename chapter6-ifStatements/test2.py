from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

a=input()
if a=="yes":
    mc.setting("world_immutable",True)
    mc.postToChat("world immutable")
else:
    mc.setting("world_immutable",False)
    mc.postToChat("world mutable")