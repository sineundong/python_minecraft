from itertools import permutations


n=int(input())
alist=[ i for i in range(1,n+1)]
print(alist)
perm=permutations(alist,n)
blist=[]
for i in perm:
    print(i)
    blist.append(list(i))
print(blist)