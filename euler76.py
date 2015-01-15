
count=0
for i8 in range(2):
    for i7 in range((9-8*i8)/7+1):
        for i6 in range((9-8*i8-7*i7)/6+1):
            for i5 in range((9-8*i8-7*i7-6*i6)/5+1):
                for i4 in range((9-8*i8-7*i7-6*i6-5*i5)/4+1):
                    for i3 in range((9-8*i8-7*i7-6*i6-5*i5-4*i4)/3+1):
                        for i2 in range((9-8*i8-7*i7-6*i6-5*i5-4*i4-3*i3)/2+1):
                            i1=9-8*i8-7*i7-6*i6-5*i5-4*i4-3*i3-2*i2
                            print i8,i7,i6,i5,i4,i3,i2,i1


#  "%s is my friend and %s is %s years old" % ('he','he',14)
#  'he is my friend and he is 14 years old'

# '-'.join(ls)

fb=open('weuler76.py','w')
fb.write('d=dict()\n')
fb.write('\n')
fb.write('\n')
ls=[]
ls2=[]
for i in range(18,1,-1):
    ls.append('i'+str(i))

for i in range(19,1,-1):
    ls2.append(str(i)+'*'+'i'+str(i))

space=2
fb.write('def run():\n')
fb.write('    for i19 in range(2):\n')

for x in range(len(ls)):
    base= "for %s in range((20-%s):" % (ls[x],'-'.join(ls2[:x+1])+')/'+ls[x].replace('i','')+'+1')
    fb.write('    '*space+base+'\n')
    space+=1

fb.write('    '*space+'i1='+'20-'+'-'.join(ls2)+'\n')
fb.write('    '*space+'count+=1\n')
fb.write('    return count')


fb.close()
