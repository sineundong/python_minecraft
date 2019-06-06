

ab=10
bb=20

def name(a,b):
    global ab,bb
    
    """
    this is name....
      
    """
    c=ab+bb
    return c
    
a=int(input())
b=int(input())
print(name(a,b))