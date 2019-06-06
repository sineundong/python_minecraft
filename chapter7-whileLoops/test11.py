alist=[]
for i in range(19):
    alistsub=list(map(int,input().split()))
    alist.append(alistsub)
    
a=int(input())
for i in range(a):
    x,y=map(int,input().split())
    
    for j in range(19):
        if alist[x-1][j]==0:
            alist[x-1][j]=1
        else:
            alist[x-1][j]=0
    for k in range(19):
        if alist[k][y-1]==0:
            alist[k][y-1]=1
        else:
            alist[k][y-1]=0
for i in alist:
    newstr=[]
    for j  in i:
        newstr.append(str(j))
    print(" ".join(newstr))