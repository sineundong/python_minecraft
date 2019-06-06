password="cat"
pass2=input("input your password :")
attemps=0
while password!=pass2 and attemps<=3:
    #attemps+=1
    pass2=input("one more your password :")
    if password==pass2:
        print("password accept")
    #else:
     
       # break
    attemps+=1
     
print("finish")