def makeprimelist(limit):
    ls=[2]
    n=3
    while n<limit:
        temp=n
        print n
        for x in ls:
            if n%x==0:
                n+=2
        if temp==n:
            ls.append(n)
            n+=2
    return ls

def replacewithx(prime,allnumbers):
    print prime
    for i in range(prime+prime,len(allnumbers)):
        if i%prime==0:
            allnumbers[i]='x'

def fullprimelist(ls,remains):
    ls2=[]
    while len(remains)>1:
        a=remains.pop(-1)
        print a
        temp=a
        for x in remains:
            if a%x==0:
                a=remains.pop(-1)
        if temp==a:
            ls2.append(a)
    ls.extend(ls2)
    return ls




def findallprimes(limit):
    allnumbers=range(limit)
    ls=makeprimelist(2000)
    for x in ls:
        replacewithx(x,allnumbers)
    #copy list
    remains=[]
    for x in allnumbers:
        if not x=='x':
            remains.append(x)
    remains.remove(0)
    remains.remove(1)
    remains=remains[len(ls):]
    print 'last step'
    return fullprimelist(ls,remains)


f=open('primes.txt')
import pickle
a=f.read()
ls=pickle.loads(a)

def checkpositive(ls):
    d=dict()
    for x in ls:
        d[x]=1
    mx=['a','b',0]
    for i in range(1,1000):
        for j in range(1,1000):
            print i, j
            n=0
            while((n**2)+(i*n)+j) in d:
                n+=1
            if n>mx[2]:
                mx[0]=i
                mx[1]=j
                mx[2]=n
    return mx


def checkall(ls):
    d=dict()
    for x in ls:
        d[x]=1
    mx=['a','b',0]
    for i in range(-999,1000):
        for j in range(-999,1000):
            print i, j
            n=0
            while((n**2)+(i*n)+j) in d:
                n+=1
            if n>mx[2]:
                mx[0]=i
                mx[1]=j
                mx[2]=n
    return mx
