import itertools

a=list(itertools.permutations(['1','2','3','4','5','6','7']))

b=[]

for x in a:
    b.append(int(''.join(x)))

f=open('primes.txt')
import pickle
a=f.read()
primes=pickle.loads(a)
del a
f.close()

def filter(b,primes):
    for i in range(len(b)):
        for x in primes:
            if b[i]=='x':
                pass
            elif b[i]%x==0:
                b[i]='x'
    bc=[]
    for x in b:
        if x!='x':
            bc.append(x)
    return bc
        
