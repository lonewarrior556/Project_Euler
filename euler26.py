def divide1by(n):
    string='0.'
    r=10
    ls=[10]
    for i in range(1500):
        a=r/n
        if r==0:
            pass
        elif a==0:
            r=r*10
            string+='0'
            ls.append('1')
        else: 
            string+=str(a)
            r=(r%n)*10
            if r in ls:
                temp=ls.index(r)
                return string, string[temp+2:]
            ls.append(r)
            
    return string, '0'

def find():
    mx=('a','a')
    n=0
    for i in range(1,1001):
        a=divide1by(i)
        if len(a[1])>len(mx[1]):
            mx=a[:]
            n=i
    return mx,n
