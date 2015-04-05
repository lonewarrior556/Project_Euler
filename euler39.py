def itri():
    ls=[]
    ls2=[]
    import math
    for i in range(1,1000):
        for j in range(1,1000-i):
            if math.sqrt(i**2+j**2)%1==0:
                ls.append((i,j,int(math.sqrt(i**2+j**2))))
    for x in ls:
        if sum(x)<1001:
            ls2.append(x)
    
    return ls2
