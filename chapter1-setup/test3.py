from mcpi.minecraft import Minecraft
mc=Minecraft.create()
naro='Have a will'
mc.postToChat(naro)
naro2 =12 

mc.postToChat("{} 12".format(naro))


naro3="{} {}".format(naro, naro2)
mc.postToChat("{}{}".format(naro, naro2))
mc.postToChat(naro3)

jenor=3
jenor2=5
print("%d %d" %(jenor, jenor2) )

name='ye chan'
age=16
print(name,' ','is',age, 'years old')
print(name+' '+'is'+str(age)+ 'years old')

