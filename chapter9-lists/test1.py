alist=["abcd",3,False]
alist[0]="bb"
print(alist)

blist=[7,28,32,45]
   # [1,2,3,1 ,2,3]
print(blist*2)

blist.index(7)
print(blist.index(7))

for i in range(len(blist)):
    print(blist[i])

for i in blist:
    print(i)
    
a="abcddddesefff"
for i in a:
    print(i)
    
for i,v in enumerate(blist):
    print(i,v)
    