f=open('primes.txt')
import pickle
primes=pickle.loads(f.read())
d=dict()
for x in primes:
    d[x]=1



def factorize(x):
    factors=[]
    while x != 1:
        for y in primes:
            if x==1:
                return factors
            if x%y==0:
                factors.append(y)
                while x%y ==0:
                    x=x/y
    return factors
    
def find():
    n=10
    while n<1000000:
        print n
        if n in d or n+1 in d or n+2 in d or n+3 in d:
            n+=1
        elif len(factorize(n))!=4:
            n+=1
        elif len(factorize(n+1))!=4:
            n+=1
        elif len(factorize(n+2))!=4:
            n+=1
        elif len(factorize(n+3))!=4:
            n+=1
        else:
            return (n,n+1,n+2,n+3)
        
        
            
    
        
