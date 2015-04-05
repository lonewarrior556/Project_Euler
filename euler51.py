f=open('primes.txt')
import pickle
primes=pickle.loads(f.read())
f.close()

d=dict()
ls=[]
for x in primes:
    if len(str(x))<6:
        pass
    elif len(set(list(str(x)[:-1]))) != len(str(x)[:-1]):
        ls.append(x)

primes=ls
del ls

for x in primes:
    d[(len(str(x)),x%10)]=d.get((len(str(x)),x%10),[])+[x]
                                       
                                                       
def check(p,v,ls):
    ls2=[]
    for x in ls:
        if int(str(x)[p])==v:
            a=list(str(x)[:-1])
            a.pop(p)
            if len(set(a)) != len(str(x))-2:
                ls2.append(x)
    return ls2

def checkall(d):
    for x in sorted(d.keys()):
        for i in range(x[0]-1):
            for j in range(10):
                ls=check(i,j,d[x])
                for k in range(i+1,x[0]-1):
                    for l in range(10):
                        a=check(k,l,ls)
                        ls2=[]
                        for m in a:
                            if 1==len(set(list(str(m)[:i]+str(m)[i+1:k]+str(m)[k+1:-1]))):
                                ls2.append(m)
                        if len(ls2) >7:
                            print x,str(i)+" = " +str(j), str(k)+" = "+str(l)
                            print ls2
                            raw_input('press when ready')
                    
        

                                        
                                            
                                             
