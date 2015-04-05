def notpali(n):
    for i in range((len(str(n))/2)+1):
        if str(n)[i]!=str(n)[-(i+1)]:
            return True
    return False

def reverse(n):
    a=''
    for i in range(len(str(n))):
        a+=str(n)[-(i+1)]
    return int(a)

pcount=0
ls=[]
for i in range(1,10001):
    count=0
    k=i+reverse(i)
    while notpali(k) and count<51:
        count+=1
        k+=reverse(k)
    if count==51:
        ls.append(i)
        print i
    
    
