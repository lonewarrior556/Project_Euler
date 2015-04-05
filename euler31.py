import math
c=[1,2,5,10,20,50,100]


def find():
    ls=[1]
    for i in range(201):
        for j in range(int(101-math.ceil(i/2.0))):
            print i,j
            for k in range(int(41-math.ceil(i/5.0))):
                for l in range(int(21-math.ceil(i/10.0))):
                    for m in range(int(11-math.ceil(i/20.0))):
                        for n in range(int(5-math.ceil(i/50.0))):
                            for o in range(int(3-math.ceil(i/100.0))):
                                if c[0]*i+c[1]*j+c[2]*k+c[3]*l+c[4]*m+c[5]*n+c[6]*o==200: ls.append(1)
#[i,j,k,l,m,n,o,0])
    return ls
