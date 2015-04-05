import itertools

a=list(itertools.permutations([1,2,3,4,5,6,7,8,9]))


def filter2d(a):
    ls=[]
    ls2=[]
    for x in a:
        if 2*int(str(x[0])+str(x[1]))==int(str(x[2])+str(x[3])):
            if 3*int(str(x[0])+str(x[1]))==int(str(x[4])+str(x[5])):
                if 4*int(str(x[0])+str(x[1]))==int(str(x[6])+str(x[7])+str(x[8])):
                    ls.append(x)
       # elif 2*int(str(x[0])+str(x[1]))==int(str(x[2])+str(x[3])+str(x[4])):
       #     ls2.append(x)
    return ls


def filter22d(a):
    ls=[]
    for x in a:
        if 2*int(str(x[0])+str(x[1]))==int(str(x[2])+str(x[3])+str(x[4])):
            if 3*int(str(x[0])+str(x[1]))==int(str(5)+str(x[6])+str(x[7])+str(x[8])):
                ls.append(ls)
    return ls

def filter3d(a):
    ls=[]
    for x in a:
        if 2*int(str(x[0])+str(x[1])+str(x[2]))==int(str(x[3])+str(x[4])+str(x[5])):
             if 3*int(str(x[0])+str(x[1])+str(x[2]))==int(str(x[6])+str(x[7])+str(x[8])):
                 ls.append(x)
    return ls

def filter4d(a):
    ls=[]
    for x in a:
         if 2*int(str(x[0])+str(x[1])+str(x[2])+str(x[3]))==int(str(x[4])+str(x[5])+str(x[6])+str(x[7])+str(x[8])):
             ls.append(x)
    return ls
