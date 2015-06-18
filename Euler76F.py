p=dict()
p[0]=1
p[1]=1

d=dict()
for i in range(1,9):
    d[i*(3*i+1)/2] = i
    d[i*(3*i-1)/2] = i

def alpha(n):

    if n == 0:
        return 1
    elif n in d:
        return pow(-1, d[n])
    else:
        return 0

def build_p(n):
    total_number = 0
    ans=[]
    arrays= []


    for i in range(n,0,-1):
        ans.append([i])


    while len(ans)>0:
            entry = ans.pop(0)
            total_number +=1
            for x in next_digits(entry,n):
                ans.append(entry + [x])
    p[n] = total_number

def next_digits(entry,n):
    total = n - sum(entry)
    maximum = entry[-1]
    if total < maximum:
        start = total
    else:
        start = maximum
    return range(start,1,-1)

for i in range(2,51):
    build_p(i)

print "p built upto 50"
print "p[50]="
print p[50]

for j in range(51,101):
    eq = "0 - ("
    for i in range(1,j+1):
        if alpha(i)!= 0:
            eq += " "+ (str(alpha(i))[0:-1]+"+")[0] + "p["+ str(j-i)+"]"
    eq +=")"
    print eq
    value = eval(eq)
    print value
    p[j]=value
