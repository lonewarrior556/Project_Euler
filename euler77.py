import pickle
p=dict()
p[0]=1
p[1]=1
f = open('primes.txt')
primes = pickle.load(f)
f.close()
primes_set = set(primes)
def top_prime(n):
    while not n in primes_set:
        n-=1
        if n<2:
            return 0
    return primes.index(n)+1


total_number = 0
def build_p(n):
    global total_number
    total_number = 0
    ans=[]
    arrays= []


    for x in reversed(primes[0:top_prime(n)]):
        ans.append([x])

    while len(ans)>0:
        entry = ans.pop(0)
        for x in next_digits(entry,n):
            ans.append(entry + [x])
    p[n] = total_number

def next_digits(entry,n):
    global total_number
    total = n - sum(entry)
    if total == 0:
        total_number += 1
        return []
    maximum = entry[-1]
    if total < maximum:
        start = total
    else:
        start = maximum
    return list(reversed(primes[0:top_prime(start)]))
