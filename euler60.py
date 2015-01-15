import itertools

f=open('primes.txt')
import pickle
ls=pickle.loads(f.read())
d=set(ls)

ls.pop(0)
ls.pop(0)
ls.pop(0)
ls.pop(0)
ls.pop(0)
f.close()



# def find(ls,d,i):
#     ls2=[ls[i]]
#     #for i in range(len(ls)):
#     for x in ls:
#         if str(x)[-1*len(str(ls[i])):]==str(ls[i]):
#             if int('0'+str(x)[:-1*len(str(ls[i]))]) in d:
#                 if int('0'+str(ls[i])+str(x)[:-1*len(str(ls[i]))]) in d:
#                     ls2.append(x)
#                     #if len(ls2)==500:
#                     #    break
#     return ls2
                
def remains(ls,i):
    ls2=[]
    for i in range(0,i+1):
        ls2.append(ls[i])
    a=ls[i]
    for x in ls[i+1:]:
        if is_prime(int('0'+str(a)+str(x))) and is_prime(int('0'+str(x)+str(a))):
            ls2.append(x)
    return ls2



def left(ls,a):
    count=0
    for x in ls:
        if is_prime(int('0'+str(a)+str(x))) and is_prime(int('0'+str(x)+str(a))):
            count+=1
            if count==5:
                return False
    return True


def sortout(ls,a):
    ls2=[]
    for x in ls:
        if is_prime(int('0'+str(a)+str(x))) and is_prime(int('0'+str(x)+str(a))) or x==a:
            ls2.append(x)                    
    return ls2

def run():
    final=[]
    ls7=ls[:]
    for x in ls7:
        print x
        if x==13:
            continue
        ls7x=sortout(ls7,x)
        for y in ls7x:
            if y<=x:
                continue
            ls7xy=sortout(ls7x,y)
            for z in ls7xy:
                if z<=y:
                    continue
                ls7xyz=sortout(ls7xy,z)
                print 13,x,y,z
                for f in ls7xyz:
                    if f <=z:
                        continue
                    if len(sortout(ls7xyz,f))!=0:
                        final.append([13,x,y,z,f])
        

    return final








def is_prime(n):
    if n<7000000:
        if n in d:
            return True
        else: return False
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



ls=ls[:3676]
ls=remains(ls,0)
