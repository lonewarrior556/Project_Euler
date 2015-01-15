ls=[0]*50
ls2=[]
summ=range(50,0,-1)
d=dict()

for x in range(0,51):
    for y in range(0,101):
        if 2*x+y<100:
            ls[-2]=x
            ls[-1]=y
            d[2*x+y]=d.get(2*x+y,[])+[ls[:]]

# sum([a + b for a, b in zip(temp, summ)])
import copy
def next_term(n):
    dval=copy.deepcopy(d.values())
    for x in dval:
        for y in x:
            for i in range(1,100/n+1):
                temp=y[:]
                temp[-n]=i
                if sum([a * b for a, b in zip(temp, summ)])<100:
                    d[sum([a * b for a, b in zip(temp, summ)])].append(temp[:])
                else: break
        
