ls3=[]
ls4=[]
ls5=[]
ls6=[]
ls7=[]
ls8=[]

a=1
n=1
while a<10000:
   a=(n*(n+1))/2 
   n+=1
   if len(str(a))==4:
       ls3.append(a)
   

a=1
n=1
while a<10000:
   a=n**2
   n+=1
   if len(str(a))==4:
       ls4.append(a)

a=1
n=1
while a<10000:
   a=(n*(3*n-2))
   n+=1
   if len(str(a))==4:
       ls8.append(a)

a=1
n=1
while a<10000:
   a=(n*(3*n-1))/2
   n+=1
   if len(str(a))==4:
       ls5.append(a)

a=1
n=1
while a<10000:
   a=n*(2*n-1)
   n+=1
   if len(str(a))==4:
       ls6.append(a)

a=1
n=1
while a<10000:
   a=(n*(5*n-3))/2
   n+=1
   if len(str(a))==4:
       ls7.append(a)

print "step 1 done"

import itertools
masterlist=list(itertools.permutations((ls3,ls4,ls5,ls6,ls7,ls8)))
 
def run():
    for ml in masterlist:
        for x3 in ml[0]:
            for x4 in ml[1]:
                if str(x3)[-2:]!=str(x4)[:2]:
                    continue
                print x3,x4
                for x5 in ml[2]:
                    if str(x4)[-2:]!=str(x5)[:2]:
                        continue
                    for x6 in ml[3]:
                        if str(x5)[-2:]!=str(x6)[:2]:
                            continue
                        for x7 in ml[4]:
                            if str(x6)[-2:]!=str(x7)[:2]:
                                continue
                            for x8 in ml[5]:
                                if str(x7)[-2:]!=str(x8)[:2]:
                                    continue
                                elif str(x8)[-2:]==str(x3)[:2]:
                                    return x3,x4,x5,x6,x7,x8
