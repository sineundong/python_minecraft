from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
firstname="eundong"
lastname="shin"
time.sleep(1)
mc.postToChat(firstname+" "+lastname)   # printf("%s",a);   print("%s" %(a))
mc.postToChat("{} {}".format(firstname,lastname))

