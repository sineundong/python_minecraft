from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
name = input("input your name :")
msg = input("message :")
mc.postToChat("your name is : {} your message is :{}".format(name,msg))
