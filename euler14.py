



def countterms(n,t=1):
    if n==1:
        return t
    elif n%2==0:
        n=n/2
        t+=1
        return countterms(n,t)
    else:
        n=3*n+1
        t+=1
        return countterms(n,t)

d=dict()

def findlongest(d):
    ls=range(1,1000000)
    longest=(0,0)
    for x in ls:
        print longest
        a=countterms2(d,x,x)
        if a>longest[0]:
            longest=(a,x)
    return longest
        


def countterms2(d,o,n,t=0):
    if o in d:
        return d[o]
    elif n==1:
        d[o]=(t+1)
        return (t+1)
    elif n in d:
        d[o]=d[n]+t
        return d[o]
    elif n%2==0:
        n=n/2
        t+=1
        return countterms2(d,o,n,t)
    else:
        n=3*n+1
        t+=1
        return countterms2(d,o,n,t)
        
