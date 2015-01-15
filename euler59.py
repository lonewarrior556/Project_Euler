ls=[]
f=open('words.txt')
a=f.readline()
while a!='':
    ls.append(a[:-2])
    a=f.readline()
f.close()

f=open('cipher1.txt')
cipher=f.read()
cipher=cipher.split(",")
f.close()

cipher1=[]
cipher2=[]
cipher3=[]

for i in range(0,len(cipher),3):
    cipher1.append(cipher[i])
for i in range(1,len(cipher),3):
    cipher2.append(cipher[i])
for i in range(2,len(cipher),3):
    cipher3.append(cipher[i])

from collections import Counter

cipher1=Counter(cipher1).most_common()[:4]
cipher2=Counter(cipher2).most_common()[:4]
cipher3=Counter(cipher3).most_common()[:4]

import math

read=''

order=[103,111,100]


key="god"

def xor(a,b):
    a=makebinary(a)
    b=makebinary(b)
    if len(a)!=len(b):
        while len(a)>len(b):
            b.append(0)
        while len(b)>len(a):
            a.append(0)
    ls=[]
    for i in range(len(a)):
        if a[i]+b[i]==1:
            ls.append(1)
        else:
            ls.append(0)
    return makenumber(ls)




def makenumber(n):
    a=0
    for i in range(len(n)):
            a= a + n[i]*(2**i)
    return a



def makebinary(n):
    if n==0:
        return [0]
    elif n==[]:
        return []
    c=[]
    b =int(math.log(n)/math.log(2))
    d= divideby2s (n,b,c)
    return d

def divideby2s (n,b,c):
    if b == -1:
        return c
    else:
        d = n/2**b
        n = n%2**b
        c= [d] + c
        b = b-1
        return divideby2s(n,b,c)


for x in cipher:
    z=xor(int(x),order[0])
    read+=str(chr(z))
    order.append(order.pop(0))


order=[103,111,100]
total=0
for x in cipher:
    z==xor(int(x),order[0])
    total+=z
    order.append(order.pop(0))
