def suma(n):
    sumnum=0
    for i in range(n+1):
        sumnum+=i
    return sumnum

def sumb(n):
    return sum((i) for i in range(n+1))

print(suma(1000))
print(sumb(1000))