
def find(a,n):
    d=dict()
    for x in a:
        d[x]=1
    for i in range(len(a)-n):
        sum2 =0
        for j in range(n):
             sum2+=a[i+j]
        if sum2 in d:
             return i,i+j
        else:
            sum2=0
    return [1000001]

def done(a):
    for i in range(545,100,-1):
        print i
        b= find(a,i)
        if b[0]<1000000:
            return b
        
