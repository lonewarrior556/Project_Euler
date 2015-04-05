import pickle

f=open('primes.txt')
a=f.read()
primes=pickle.loads(a)
del a
f.close()

d=dict()
for x in primes:
    d[x]=1

n=9

def upto(n,limit):
    import math
    if n in d:
        pass
    else:
        while n<limit:
            i=0
            while n>primes[i]:
                if n in d:
                    n+=2
                    i=0
                if math.sqrt((n-primes[i])/2)%1==0:
                    n+=2
                    i=0
                else:
                    i+=1
            return n
