from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

#immutable :change X
#mc.setting("world_immutable",True)
mc.setting("world_immutable",False)


#print(True)
#print("true")