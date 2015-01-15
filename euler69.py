import pickle

f=open('primes.txt')
primes=pickle.loads(f.read())

def filter(ls):
    ls2=[]
    for x in ls:
        if x<1000001:
            ls2.append(x)
        else: return ls2

primes=filter(primes)
primeset=set(primes)

f.close()
def factorout(n,x):
    if n%x!=0:
        return n
    else:
        return factorout(n/x,x)

def prime_fact(n):
    facts=[]
    if True:
        for x in primes:
            if n%x==0:
                facts.append(x)
                n=factorout(n,x)
                if n in primeset:
                    facts.append(n)
                    return facts
                elif n==1:
                    return facts


def diction():
    d=dict()
    for x in range(2,1000001):
        if x in primeset:
            d[x]=set([x])
        else:

            d[x]=set(prime_fact(x))
    return d

d=diction()


def rprime(n,d):
   # rp=[1]
    rp=1
    ls=d[n]
    for i in range(2,n):
        if len(ls.intersection(d[i]))==0:
           # rp.append(i)
            rp+=1
    return float(n)/rp

top=[4.8125,2310]        
            
def test(top,n=20071):
    for x in range(n,1000001,2):
        if rprime(x,d)>top[0]:
            top[0]=rprime(x,d)
            top[1]=x
            print x
