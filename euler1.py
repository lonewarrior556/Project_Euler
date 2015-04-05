n=str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

def product(n):
    answer=0
    for i in range(len(n)-4):
        product = int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])
        if product > answer:
            answer=product
    return answer


import math

#a + b + c =1000
#a^2 + b^2 = C^2
def findnumbers():
    b=0
    for i in range(1,500):
        b=i
        while 2*b< 1000-i:
            b+=1
            temp=math.sqrt(i**2 + b**2)
            if temp == int(temp):
                print 'a='+str(i),'b='+str(b), 'c='+ str(temp)
                print 'a+b+c = ', i+b+temp
                if i+b+temp==1000:
                    return True

def makeprimelist(limit):
    ls=[2]
    n=3
    while n<limit:
        temp=n
        print n
        for x in ls:
            if n%x==0:
                n+=2
        if temp==n:
            ls.append(n)
            n+=2
    return ls

def replacewithx(prime,allnumbers):
    print prime
    for i in range(prime+prime,len(allnumbers)):
        if i%prime==0:
            allnumbers[i]='x'

def fullprimelist(ls,remains):
    ls2=[]
    while len(remains)>1:
        a=remains.pop(-1)
        temp=a
        for x in remains:
            if a%x==0:
                a=remains.pop(-1)
        if temp==a:
            ls2.append(a)
    ls.extend(ls2)
    return ls
        
    





def findallprimes(limit):
    allnumbers=range(limit)
    ls=makeprimelist(500)
    for x in ls:
        replacewithx(x,allnumbers)
    #copy list
    remains=[]
    for x in allnumbers:
        if not x=='x':
            remains.append(x)
    remains.remove(0)
    remains.remove(1)
    remains=remains[len(ls):]
    return fullprimelist(la,remains)






        
    
