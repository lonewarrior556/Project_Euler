def rest(n,a=(1,2,3,4,5,6,7,8,9)):
    a=list(a)
    for x in str(n):
        a.remove(int(x))
    return a


def pandigitallist():
    ls=[]
    for i in range(2789,9877):
        if '0' in str(i):
            pass
        elif len(str(i))== len(set(map(int,str(i)))):
            ls.append(i)
    return ls

def available(ls):
    d=dict()
    for x in ls:
        d[tuple(rest(x))]=1
    return d

def combine(t):
    return int(''.join(map(str,t)))

import itertools

def finall():
    finish=[]
    ls=pandigitallist()
    answers=dict()
    for x in ls:
        answers[tuple(rest(x))]=answers.get(tuple(rest(x)),[])+[x]
    d=available(ls)
    d=d.keys()
    
    for x in d:
        print x
        b=list(itertools.permutations(x))
        for y in b:
            if combine(y[:3])*combine(y[-2:]) in answers[x]:
                finish.append(combine(y[:3])*combine(y[-2:]))
            if combine(y[:4])*y[-1] in answers[x]:
                finish.append(combine(y[:4])*y[-1])
                
    f=dict()
    for x in finish:
        f[x]=1
    finish=f.keys()
    return finish
