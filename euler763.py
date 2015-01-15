d=dict()
d[1]=1
d[2]=2


d[3]=d[2]+1

d[4]=d[3]+d[2]+1

def run(n):
    if n in d:
        return d[n]
    total=0
    for i in range(n-1,n/2,-1):
        total+=d[i]
    d[n]=total
    return total

