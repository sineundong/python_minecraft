a=int(input())
alist=[]
for i in range(a):
    m=int(input())
    alist.append(m)
#print(alist)
alist.reverse()
#print(alist)
count=0
clist=[]
maxnum=alist[0]
for i in alist:
    if i>=alist[0]:
        if i>=maxnum:
            maxnum=i
            count+=1  # count=count+1
            clist.append(i)
#print(count-1)
#print(clist)
print(len(clist)-1)