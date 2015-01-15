def equals(n):
    if abs(n-int(n))>.99999 or abs(n-int(n))<.00001:
        return True
    else: return False

def run():
    count=0
    i=1
    while i<43000000:
        if equals(pow(i,1.0/len(str(i)))):
            print i
            count+=1
        i+=1
    return count


def meta2():
    count=0
    import math
    for i in range(2,10):
        for n in range(1,1000):
            if (n-1)/float(n)<=math.log10(i):
                count+=1
    return count
