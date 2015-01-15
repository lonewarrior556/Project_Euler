f=open('triangle.txt')

ls=[]
 

a=f.readline()
while a!='':
    a=a[:-1]
    a=a.split()
    for i in range(len(a)):
        a[i]=int(a[i])
    ls.append(a)
    a=f.readline()



def addlastrow(ls):
    a=ls[len(ls)-1]
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            ls[len(ls)-2][i]=ls[len(ls)-2][i]+a[i]
        else: 
            ls[len(ls)-2][i]=ls[len(ls)-2][i]+a[i+1]
