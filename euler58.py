f=open('primes.txt')
import pickle
primes=pickle.loads(f.read())
d=dict()
for x in primes:
    d[x]=1
f.close()

def makebox(n):
    ls=[]
    for i in range(n+1):
        ls.append([])
    temp=ls[:]
    for i in range(len(ls)):
        ls[i]=temp[:]
    order=['r','u','l','d']
    start=(n/2)
    steps=1
    a=start
    b=start
    c=1
    ls[a][b]=c
    while c<(n*n):
        for i in range(2):
            if order[0]=='r':
                for i in range(steps):
                    b+=1
                    c+=1
                    if a==b or (-1*b)+n-1 ==a:
                        ls[a][b]=c
            elif order[0]=='d':
                for i in range(steps):
                    a+=1
                    c+=1
                    if a==b or (-1*b)+n-1 ==a:
                        ls[a][b]=c
            elif order[0]=='l':
                for i in range(steps):
                    b-=1
                    c+=1
                    if a==b or (-1*b)+n-1 ==a:
                        ls[a][b]=c
            elif order[0]=='u':
                for i in range(steps):
                    a-=1
                    c+=1
                    if a==b or (-1*b)+n-1==a:
                        ls[a][b]=c
            order.append(order.pop(0))

        steps+=1
    for i in range(n):
        ls[i].pop(-1)
    ls.pop(-1)
#    for i in range(n):
#        print ls[i]
    return ls

# if a==b or (-1*b)+n-1 ==a:




def count(ls):
    top=0
    for i in range(len(ls)/2):
        if ls[i][i] in d:
            top+=1
    for i in range(len(ls)):
        if ls[len(ls)-i-1][i] in d:
            top+=1
    print [top,len(ls)*2-1]
    return top/float((len(ls)*2)-1)



def all():
    n=1441
    ls=[]
    while n<30000:
        print n
        if count(makebox(n))<.1:
            return n
        n+=2
    

def meta2():
        import math
	count=0
        n1=(count**2)+1-count
        n2=n1+count
        n3=n2+count
	primes=0
	length=1
	while length< math.sqrt(6500000):
            n1=(count**2)+1-count
            n2=n1+count
            n3=n2+count
            ls=[n1,n2,n3]
            for x in ls:
                if x in d:
                    primes+=1
            length+=2
            count+=2
        return meta3(count,primes,length)

def meta3(count,primes,length):
    while (primes/float((length*2)-1))>.1:
        print length,(primes/float(length*2-1))
        n1=(count**2)+1-count
        n2=n1+count
        n3=n2+count
        ls=[n1,n2,n3]
        for x in ls:
            if x%3==0 or x%5==0 or x%7==0 or x%11==0 or x%13==0:
                pass
            elif is_prime(x):
                primes+=1
                print "got a prime "+str(x)
        length+=2
        count+=2
    return length


def is_prime(n):
    import random
    temp=n-1
    nof2=0
    while temp%2==0:
        temp=temp/2
        nof2+=1
    test=[True,]+[]*20+[False]
    for i in range(1,len(test)):
        if test[i-1] and not test[-1]:
            a=random.randint(2,n-1)
            v=pow(a,temp,n)
            if v==1 or v==n-1:
                test[i]=True
            else:
                ls=[]
                for z in range(1,nof2):
                    ls.append(2**z)
                for k in ls:
                    v=pow(a,temp*k,n)
                    if v==n-1:
                        test[i]=True
                        break     
                    
    if test[-1]==True:
        return True
    else: return False
