from decimal import *
getcontext().prec = 5000

def sqrtf(n):
    a=Decimal(n).sqrt()
    ls=[int(a)]
    check=[str(a)[:7]]
    rest=a%1
    for i in range(10000):
        if i==9999:
            print "ERROR", n
            print "ERROR", n
            print "ERROR", n
            print "ERROR", n
            raw_input()
        a=1/rest
        rest=a%1
        if str(a)[:7] in check:
            check.append(str(a)[:7])
            break
        else:
            check.append(str(a)[:7])
        ls.append(int(a))

    
    return ls


def counter():
    count=0
    toss=[]
    for i in range(1,10001):
        print i
        try:
            if len(sqrtf(i))%2==0:
                count+=1
        except:
            toss.append(i)
            continue
    return count



def superroot(a):
    n=0
    ls=[]
    for x in range(0,100):
        ls.append(pow(10,x))
    for i in ls:
        while n*n<a:
            print n
            if (n+(1.0/i))**2>a:
                break
            else: n+=(1.0/i)
    return n
