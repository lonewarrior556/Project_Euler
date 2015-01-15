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
def mktrinums(limit):
    ls=[1]*limit
    for i in range (1,limit):
        ls[i]=ls[i-1]+i+1
    return ls

def divisors(n):
    c=2
    divisorb=[1]
    divisort=[n]
    while c<divisort[0]:
        if n%c==0:
            divisorb.append(c)
            divisort=[n/c]+divisort
        c+=1
    divisor=divisorb+divisort
    return divisor 

def mostdivisors(limit):
    ls=mktrinums(limit)
    d=(0,0)
    for x in ls:
        print x
        a=divisors(x)
        if len(a)>d[0]:
            d=(len(a),a[-1])
    return d

def find500():
    ls=mktrinums(20000)
    for x in ls:
        print x
        a=divisors(x)
        if len(a)>500:
            return x
