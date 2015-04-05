import pickle
f=open('primes.txt')
primes=pickle.loads(f.read())
primes=primes[:primes.index(1000003)]


primeset=set(primes)
f.close()

def factlist(n):
    facts=[]
    for x in primes:
        if n%x==0:
            while n%x==0:
                facts.append(x)
                n=n/x
            if n in primeset or n in d2:
                facts.append(n)
                return facts
            if n==1:
                return facts
    
d2=dict()

for x in primes:
    d2[x]=x-1

def reprime2(n,d2):
    ls=factlist(n)
    ans=1
    for x in ls:
        ans=ans*d2[x]
    d2[n]=ans
    return ans

def run():
    ls=[]
    for i in range(2,1000000):
        if i in primeset:
            pass
        else:
            if sorted(list(str(reprime2(i,d2))))==sorted(list(str(i))):
                ls.append(i)
                print i
    return ls

ls=run()
