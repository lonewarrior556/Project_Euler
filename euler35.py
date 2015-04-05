f=open('primes.txt')
a=f.read()
f.close()
import pickle
ls=pickle.loads(a)

def ls2d(ls):
    d=dict()
    for x in ls:
        a=list(str(x))
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[x]
    return toss(d)

def toss(d):
    d2=dict()
    d2[('2',)]=[2]
    d2[('5',)]=[5]
    for x in d.keys():
        if len(x)>len(d.get(x)):
            pass
        elif '5' in x:
            pass
        elif '0' in x:
            pass
        elif '2' in x:
            pass
        else:
            d2[x]=d.get(x)
    return d2

def allrotated(n):
    ls=[]
    for i in range(len(str(n))):
        a=str(n)[1:]+str(n)[0]
        n=int(a)
        ls.append(n)
        
    return ls


def finall():
    d=ls2d(ls)
    answer=[11]
    for x in d.keys():
        a=d[x]
        for y in a:
            print y
            if set(allrotated(y)).issubset(a):
                answer.append(y)
    return answer
