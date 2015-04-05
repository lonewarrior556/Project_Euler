

def makebox(n):
    ls=[]
    for i in range(n+1):
        ls.append([])
    temp=ls[:]
    for i in range(len(ls)):
        ls[i]=temp[:]
    order=['r','d','l','u']
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
                    ls[a][b]=c
            elif order[0]=='d':
                for i in range(steps):
                    a+=1
                    c+=1
                    ls[a][b]=c
            elif order[0]=='l':
                for i in range(steps):
                    b-=1
                    c+=1
                    ls[a][b]=c
            elif order[0]=='u':
                for i in range(steps):
                    a-=1
                    c+=1
                    ls[a][b]=c
            order.append(order.pop(0))
        
        steps+=1
    for i in range(n):
        ls[i].pop(-1)
    ls.pop(-1)
#    for i in range(n):
#        print ls[i]
    return ls


def summed(box):
    n=0
    for i in range(len(box)):
        n+=box[i][i]
    for i in range(len(box)):
        n+=box[len(box)-1-i][i]
    n-=1
    return n

