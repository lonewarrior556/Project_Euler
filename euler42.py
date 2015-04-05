d=dict()
ls=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n=1
for x in ls:
    d[x]=n
    n+=1

n=0

tri=[]
while n<300:
    temp=(n**2+n)/2
    tri.append(temp)
    n+=1

dtri=dict()
for x in tri:
    dtri[x]=1



f=open('words.txt')
a=f.read()
f.close()
a=a.split("\",\"")
a[0]=a[0][1:]
a[-1]=a[-1][:-1]

answer=[]
for x in a:
    summ=0
    for y in x:
        summ+=d[y]
    if summ in dtri:
        answer.append(x)

print len(answer)
        
