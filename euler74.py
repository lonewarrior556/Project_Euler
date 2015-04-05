import math
d=dict()
for x in range(10):
    d[str(x)]=math.factorial(x)


def factorial(s):
    total=0
    for x in s:
        total+=d[x]
    return str(total)


def run():
    ls=[]
    for i in range(2,1000001):
        n=str(i)
        nset=set()
        nset.add(n)
        for j in range(60):
            n=factorial(n)
            if n in nset:
                if j==59:
                    print i
                    ls.append(i)
                break
            else:
                nset.add(n)
    return ls
