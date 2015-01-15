def divisors(n):
    c=2
    divisorb=[1]
    divisort=[n]
    while c<divisort[0]:
        if n%c==0:
            divisorb.append(c)
            divisort=[n/c]+divisort
        c+=1
    if divisorb[-1]==divisort[0]:
        divisort=divisort[1:]
    divisor=(divisorb+divisort[:-1])
    return divisor



#######################

#find all numbers that cannot be made as a sum of all abundant numbers


def abn():
    ls=[]
    for i in range(1,28125):
        print i
        if sum(divisors(i))>i:
            ls.append(i)
    ls.append(99999)
    return ls


def find(ls):
    d=dict()
    for x in ls:
        d[x]=1
    n=1
    ls2=[]
    while n<28124:
        print n
        i=0
        while ls[i]<n:
            if (n-ls[i]) in d:
                n+=1
                i=0
            else:
                i+=1
        ls2.append(n)
        n+=1
    return ls2
