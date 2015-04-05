def summed(n):
    tot=0
    for x in str(n):
        tot+=int(x)
    return tot

record=[0,0,0]

for i in range(1,101):
    print i
    p=i
    for j in range(1,101):
        b=summed(p)
        if b>record[2]:
            record=[i,j,b]
        p=p*i
        
