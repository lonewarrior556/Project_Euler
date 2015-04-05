def makep(limit):
    ls=[]
    n=0
    while n<limit:
        ls.append(n*(3*n-1)/2)
        n+=1
    return ls

def run():
    ls=makep(1000)
    d=dict()
    for x in ls:
        d[x]=1
    
def plus(limit):
    ls=[]
    for i in range(1,limit):
        print i
        for j in range(1,i):
            for k in range(1,i):
                if 3*((i**2)-(j**2)-(k**2))==i-j-k:
                    ls.append([i,j,k])
    return ls

def minus(ls,limit):
    ls=[]
    for x in ls:
        i=x[0]
        j=x[1]
        for n in range(1,limit):
            if (3*(i**2)-i)-(3*(j**2)+j)==3*(n**2)-n:
                return i,j
                
def allplus(limit):
    ls=[]
    import math
    for i in range(1,limit):
        print i
        for j in range(1,i):
            if ((math.sqrt(36*(i**2)-(12*i)+36*(j**2)-(12*j)+1)+1)/6.0)%1==0:
                ls.append([i,j])
    return ls

def testminus(ls):
    l=[]
    import math
    for x in ls:
        i=x[0]
        j=x[1]
        print i,j
        if ((math.sqrt(36*(i**2)-(12*i)-36*(j**2)+(12*j)+1)+1)/6.0)%1==0:
            l.append(x)
    return l

        
