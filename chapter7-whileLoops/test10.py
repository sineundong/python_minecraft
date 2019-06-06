#===============================================================================
# alist=[]
# for i in range(19):
#     alistsub=[]
#     for j in range(19):
#         alistsub.append(0)
#     alist.append(alistsub)
# print(alist)
#===============================================================================

alist=[[0 for i in range(19)] for j in range(19)]
a=int(input())
for i in range(a):
    n,m=map(int,input().split())
    alist[n-1][m-1]=1




for i in alist:
    newstr=[]
    for j  in i:
        newstr.append(str(j))
    print(" ".join(newstr))  
    