# from decimal import *
# getcontext().per = 100


# ls=[]
# for i in range(1,32):
#     ls.append(i**2)


# def run():
#     mx=0
#     md=0
#     for D in range(1,1001):
#         print D
#         if D in ls:
#             pass
#         else:
#             x=int(math.sqrt(D))
#             test=True
#             while test:
#                 for y in range(1,int((pow(x,2)/float(D)))):
#                     if pow(x,2)-D*pow(y,2)==1:
#                         if x>mx:
#                             mx=x
#                             md=D
#                         test=False
#                         break
#                 x+=1
#     return mx,md
        
# def meta2():
#     md=0
#     mx=0
#     for D in range(1,1001):
#         print D,md
#         if D in ls:
#             pass
#         else:
#             y=1
#             while True:
#                 if y%10 in [2,3,7,8]:
#                     pass
#                 elif Decimal(1+D*pow(y,2)).sqrt()%1==0:
#                     x=1+D*pow(y,2)
#                     if x>mx:
#                         mx=x
#                         md=D
#                     break
#                 y+=1
#     return mx,md

#above won't work
from euler64 import *
#sqrtf(n) gives repeating roots
sl=[]
for x in range(1,31):
    sl.append(pow(x,2))



def runit():
    maxx_i=[0,0]
    for i in range(60,1001):
        if i in sl:
            continue
        print i
        ls=sqrtf(i)
        ls=ls+ls[1:]*1000
        b=test(ls,i,[])
        if b>maxx_i[0]:
            maxx_i=[b,i]
            print maxx_i
    return maxx_i


def test(ls,i,seq):
    seq.append(ls.pop(0))
    if len(seq)==1:
        seq.append(ls.pop(0))
    a=makestring(seq[0],seq[1:])
    a=eval_last(a)
    if (pow(a[0],2)-i*pow(a[1],2))==1:
        seq=[]
        return a[0]
    else: return test(ls,i,seq)
                     


def makestring(first,seq):
    beg=str(first)+'+1/'
    if len(seq)==1:
        return beg+str(seq[0])
    for x in seq[:-1]:
        beg= beg+'('+str(x)+'+1/'
    beg=beg+str(seq[-1])
    return beg
    


def eval_last(string):
    if not '(' in string:
        a=string.find('/')
        top=int(string[a+1:])*int(string[:string.find('+')])+int(string[2:a])
        return top, int(string[a+1:])
    a=string.rfind('+')
    b=string.rfind("/")
    den=int(string[b+1:])
    c=string.rfind('/(')
    d=string.rfind('+')
    num=int(string[a+1:b])+int(string[c+2:d])*den
    string=string[:c]
    string=string[:string.rfind('+')+1]
    return eval_last(string+str(den)+'/'+str(num))

import sys
import resource
 
# Increase max stack size from 8MB to 512MB
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
