from math import *
def is_mirror(n):
    for i in range(len(n)/2):
        if n[i]==n[-1-i]:
            pass
        else: return False
    return True

ls=[]
for i in range(1,1000000):
    if is_mirror(list(str(i))):
        ls.append(i)


def makebinary(n):
    if n==0:
        return [0]
    elif n==[]:
        return []
    c=[]
    b =int(log(n)/log(2))
    d= divideby2s (n,b,c)
    return d

def divideby2s (n,b,c):
    if b == -1:
        return c
    else:
        d = n/2**b
        n = n%2**b
        c= [d] + c
        b = b-1
        return divideby2s(n,b,c)
