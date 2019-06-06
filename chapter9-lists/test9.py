def getdateturple(str):
    n=str.split("-")
    y=int(n[0])
    m=int(n[1])
    d=int(n[2])
    return y,m,d


def getdateturple2(str):
    y=int(str[0:4])
    m=int(str[5:7])
    d=int(str[8:10])
    return y,m,d


a="2018-01-21"
print(getdateturple(a))

print(getdateturple2(a))