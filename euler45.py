def trilist(limit):
    ls=[]
    for i in range(limit):
        ls.append((i*(i+1))/2)
    return ls

def checkp(ls):
    ls2=[]
    import math
    for x in ls:
        if ((math.sqrt(24*x+1)+1)/6.0)%1==0:
            ls2.append(x)
    return ls2

def checkh(ls):
    ls2=[]
    import math
    for x in ls:
        if ((math.sqrt(8*x+1)+1)/4.0)%1==0:
            ls2.append(x)
    return ls2


def find(limit):
    ls=trilist(limit)
    ls=checkp(ls)
    ls=checkh(ls)
    return ls
