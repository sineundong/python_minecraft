from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

time.sleep(10)


blockhits=mc.events.pollBlockHits()

a="{}".format(blockhits)
print(a)


mc.postToChat(" hahahahahahah your score is:"+str(len(blockhits)))

