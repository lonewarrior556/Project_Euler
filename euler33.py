#ef reduce(n,d):




def mklist():
    ls=[]
    for i in range (10,100):
        for j in range(10,100):
            if i==j:
                pass
            elif i%10==0 or j%10==0:
                pass
            else:
                if str(i)[0]in str(j) or str(i)[1] in str(j):
                    ls.append([i,j])
    l=[]
    for x in ls:
        if not x[0]/float(x[1])>=1:
            l.append(x)
    l.sort()
    return l


def removecommon(nl):
    if str(nl[0])[0] in str(nl[1]):
        return nl[0]%10,int(float(str(nl[1]).replace(str(nl[0])[0],'',1)))
    elif str(nl[0])[1] in str(nl[1]):
        return nl[0]/10,int(float(str(nl[1]).replace(str(nl[0])[1],'',1)))


def finall(ls):
    answer=[]
    for x in ls:
        if x[0]/float(x[1]) == removecommon(x)[0]/float(removecommon(x)[1]):
                          answer.append(x)
    return answer
