def makeprimelist(limit):
    ls=[2]
    n=3
    while n<limit:
        temp=n
        print n
        for x in ls:
            if n%x==0:
                n+=2
        if temp==n:
            ls.append(n)
            n+=2
    return ls

def replacewithx(prime,allnumbers):
    print prime
    for i in range(prime+prime,len(allnumbers)):
        if i%prime==0:
            allnumbers[i]='x'

def fullprimelist(ls,remains):
    ls2=[]
    a=remains.pop(-1)
    while len(remains)>=1:
        temp=a
        for x in remains:
            if a%x==0:
                a=remains.pop(-1)
        if temp==a:
            ls2.append(a)
            a=remains.pop(-1)
    ls2.append(a)
    
    ls.extend(ls2)
    return ls
        
    

def findallprimes(limit):
    allnumbers=range(limit)
    ls=makeprimelist(500)
    for x in ls:
        replacewithx(x,allnumbers)
    #copy list
    remains=[]
    for x in allnumbers:
        if not x=='x':
            remains.append(x)
    remains.remove(0)
    remains.remove(1)
    remains=remains[len(ls):]
    return fullprimelist(ls,remains)

def allprimes():
    ls=range(2000000)
    ls[0]='x'
    ls[1]='x'
    for x in ls:
        if x=='x':
            pass
        else:
            n=2*x
            while n<2000000:
                ls[n]='x'
                n+=x
    ls2=[]
    for x in ls:
        if not x=='x':
            ls2.append(x)
    return ls2
