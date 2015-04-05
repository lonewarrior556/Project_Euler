import itertools
ls=list(itertools.permutations([1,2,3,4,5,6,7,8,9,10]))
def check(a):
    if a[0]+a[1]+a[3]==a[2]+a[3]+a[5]==a[4]+a[5]+a[7]==a[6]+a[7]+a[8]==a[9]+a[8]+a[1]:
        return True
    else: return False

def filter(ls):
    ls2=[]
    for x in ls:
        if check(x):
                ls2.append(x)
    ls3=[]
    for y in ls2:
        if not 10 in [y[1],y[3],y[5],y[7],y[8]]:
            ls3.append(y)
    ls4=[]
    for x in ls3:
        if x[0]<x[2] and x[0]<x[4] and x[0]<x[6] and x[0]<x[9]:
            ls4.append(x)
    ls5=[]
    for x in ls4:
        ls5.append(str(x[0])+str(x[1])+str(x[3])+str(x[2])+str(x[3])+str(x[5])+str(x[4])+str(x[5])+str(x[7])+str(x[6])+str(x[7])+str(x[8])+str(x[9])+str(x[8])+str(x[1]))
    return ls5
