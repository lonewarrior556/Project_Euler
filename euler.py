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
    a=remains.pop(-1)
    while len(remains)>=1:
        temp=a
        for x in remains:
            if a%x==0:
                a=remains.pop(-1)
        if temp==a:
            ls2.append(a)
            a=remains.pop(-1)
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
    return fullprimelist(ls,remains)

def allprimes(limit):
    ls=range(limit)
    ls[0]='x'
    ls[1]='x'
    for x in ls:
        if x=='x':
            pass
        else:
            n=2*x
            while n<limit:
                ls[n]='x'
		n+=x
    ls2=[]
    for x in ls:
        if not x=='x':
            ls2.append(x)
    return ls2


############################# num 11
a="08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

a=a.split('\n')

for i in range(len(a)):
    a[i]=a[i].split()

for i in range(20):
    for j in range(20):
        a[i][j]=int(a[i][j])

def largestproductrow(a):
    product=0
    for i in range(20):
        for j in range(1):
            temp=a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
            if temp>product:
                product=temp
    return product
            
def largestproductcol(a):
    product=0
    for i in range(17):
        for j in range(20):
            temp=a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
            if temp>product:
                product=temp
    return product

def largestproductdiag(a):
    product=0
    for i in range (17):
        for j in range (17):
            temp=a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
            if temp>product:
                product=temp
    return product

def largestproductdiagx(a):
    product=0
    for i in range (3,20):
        for j in range (0,17):
            temp=a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3]
            if temp>product:
                product=temp
    return product


