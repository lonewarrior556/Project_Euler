



def fifth(limit):
    ls=[]
    for i in range(2,limit):
        total=0
        for x in str(i):
            total+=int(x)**5
        if total==i:
            ls.append(i)
    return ls
