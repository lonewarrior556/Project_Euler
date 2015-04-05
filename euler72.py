f=open('primes.txt')
import pickle
primes=pickle.loads(f.read())
f.close()
primes=primes[:primes.index(1000003)]
primeset=set(primes)

import math

d=dict()

for x in primes:
    d[x]=x-1


for x in primes:
    for i in range(1,int(math.log(1000001)/math.log(x))+1):
        d[pow(x,i)]=d[x]*pow(x,i-1)


def factor(n):
    ls=[]
    for x in primes:
        if n%x==0:
            t=1
            while n%pow(x,t)==0:
                t+=1
            n=n/pow(x,t-1)
            ls.append(pow(x,t-1))
            if n in primeset or d:
                ls.append(n)
                return ls
            elif n==1:
                return ls


def rel_primes(n):
    if n in d:
        return d[n]
    else:
        ls=factor(n)
        tot=1
        for x in ls:
            tot=tot*d[x]
        d[n]=tot
        return tot

def run():
    total=0
    for i in range(2,1000001):
        total+=rel_primes(i)
    return total
        
            
