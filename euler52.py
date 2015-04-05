
def find(limit):
    ls=[]
    for i in range(1,limit):
        for j in range(int(str(1)+(i*str(0))),int(str(1)+(i*str(6)))+1):
            if set(str(j))==set(str(6*j)):
                if set(str(j))==set(str(2*j)):
                    ls.append([j])
    return ls
                
