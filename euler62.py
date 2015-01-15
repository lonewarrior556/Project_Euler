ls=[]

for i in range(10000):
    ls.append(tuple(list(str(i**3))))

setls=set(ls)


import itertools

def run():
    for x in ls:
        a=list(itertools.permutations(x))
        count=[]
        for y in a:
            if y[0]=='0':
                continue
            if y in setls and not y in count:
                count.append(y)
                if len(count) ==5:
                    answer=[]
                    for z in count:
                        answer.append(int(''.join(map(str,z))))
                        return answer
    return "need larger range"


def meta2():
    d=dict()
    for x in setls:
        d[(frozenset(x),len(x))]=d.get((frozenset(x),len(x)),[])+[x]
    for z in d.keys():
        if len(d[z])<5:
            d.pop(z)
    return d
            
def permulist(ll):
    import collections
    ls2=[]
    for x in ll:
        ls2.append(tuple(sorted(list(x))))
    if collections.Counter(ls2).most_common()[0][1]>4:
        return True
    else:
        return False               
    
def meta3():
    d=dict()
    answer=[]
    for x in ls:
        d[tuple(sorted(list(x)))]=d.get(tuple(sorted(list(x))),0)+1
        if d.get(tuple(sorted(list(x))))==5:
            answer.append(x)
    return answer
