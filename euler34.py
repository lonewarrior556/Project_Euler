def find(start,limit):
    import math
    ls=[145,40585]
    for x in range(start,limit):
        summed=0
        for y in str(x):
            summed+=math.factorial(int(y))
        if summed==x:
            ls.append(x)
    return ls
