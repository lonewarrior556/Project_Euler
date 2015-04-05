


def find(n):
    count=0
    for i in range(5,n/2):
        for j in range(1,(n-i)/2+1):
            k=n-i-j
            if pow(i,2)==pow(j,2)+pow(k,2):
                count+=1
                print j,k,i
                if count>1:
                    return False
    if count==1:
        return True
    else: return False

d=dict()

def find2():
    ls=[]
    for n in range(2,866):
        for m in range(1,n):
            a=pow(n,2)-pow(m,2)
            b=2*n*m
            c=pow(n,2)+pow(m,2)
            d[a+b+c]=d.get((a+b+c),[])+[tuple(sorted([a,b,c]))]
            t=2
            top=1500000/(a+b+c)
            while t<=top:
                d[t*(a+b+c)]=d.get(t*(a+b+c),[])+[tuple(sorted([t*a,t*b,t*c]))]
                t+=1
            print n



