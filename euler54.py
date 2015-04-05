f=open('poker.txt')

h1=[]
h2=[]
a=f.readline()
while a!='':
    h1.append(a[:14])
    h2.append(a[15:-1])
    a=f.readline()
f.close()

l1=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
l2=['02','03','04','05','06','07','08','09','10','11','12','13','14']
ll=zip(l1,l2)

for i in range(len(h1)):
    for x in ll:
        h1[i]=h1[i].replace(x[0],x[1])
        h2[i]=h2[i].replace(x[0],x[1])

for i in range(len(h1)):
    if h1[i].count('C')==5:
        h1[i]=('Y', sorted(h1[i].replace('C','').split(' '),reverse=True))
    elif  h1[i].count('D')==5:
        h1[i]=('Y', sorted(h1[i].replace('D','').split(' '),reverse=True))
    elif  h1[i].count('H')==5:
        h1[i]=('Y', sorted(h1[i].replace('H','').split(' '),reverse=True))
    elif  h1[i].count('S')==5:
        h1[i]=('Y', sorted(h1[i].replace('S','').split(' '),reverse=True))
    else:
        h1[i]=('N', sorted(h1[i].replace('S','').replace('H','').replace('D','').replace('C','').split(' '),reverse=True))

for i in range(len(h2)):
    if h2[i].count('C')==5:
        h2[i]=('Y', sorted(h2[i].replace('C','').split(' '),reverse=True))
    elif  h2[i].count('D')==5:
        h2[i]=('Y', sorted(h2[i].replace('D','').split(' '),reverse=True))
    elif  h2[i].count('H')==5:
        h2[i]=('Y', sorted(h2[i].replace('H','').split(' '),reverse=True))
    elif  h2[i].count('S')==5:
        h2[i]=('Y', sorted(h2[i].replace('S','').split(' '),reverse=True))
    else:
        h2[i]=('N', sorted(h2[i].replace('S','').replace('H','').replace('D','').replace('C','').split(' '),reverse=True))
       

def compare():
    p1=0
    ls=[h1,h2]
    for j in ['14','13','12','11','10','09','08','07','06']:
        c=0
        for x in ls:
            c+=1
            for i in range(len(h1)):
                if x[i][0]=='Y':
                    if int(x[i][1][0])-int(x[i][1][4])==4:
                        if x[i][1][0]==j:
                            if c==1:
                                p1+1
                            h1.pop(i)
                            h2.pop(i)
    print p1
    for j in ['14','13','12','11','10','09','08','07','06','05','04','03','02']:
        c=0
        for x in ls:
            c+=1
            for i in range(len(h1)):
                if len(set(x[i][1]))==2:
                    if x[i][1][1]==x[i][1][4] or x[i][1][0]==x[i][1][3]:
                        if x[i][1][1]==j:
                            if c==1:
                                p1+=1
                            h1[i]='x'
                            h2[i]='x'
    print p1
    for j in ['14','13','12','11','10','09','08','07','06','05','04','03','02']:
        c=0
        for x in ls:
            c+=1
            for i in range(len(h1)):
                if x[i]=='x':
                    pass
                elif len(set(x[i][1]))==2:
                    if x[i][1][2]==j:
                        print h1[i],h2[i]
                        if c==1:
                            p1+=1
                        h1[i]='x'
                        h2[i]='x'
    for j in ['14','13','12','11','10','09','08','07','06','05','04','03','02']:
        c=0
        for x in ls:
            c+=1
            for i in range(len(h1)):
                if x[i]=='x':
                    pass
                #there is an error here where it only considers the first card
                elif x[i][0]=='Y' and x[i][1][0]==j:
                    print h1[i],h2[i]
                    if c==1:
                        p1+=1
                    h1[i]='x'
                    h2[i]='x'

    for j in ['14','13','12','11','10','09','08','07','06']:
        c=0
        for x in ls:
            c+=1
            for i in range(len(h1)):
                if x[i]=='x':
                    pass
                elif int(x[i][1][0])-int(x[i][1][4])==4 and len(set(x[i][1]))==5:
                        if x[i][1][0]==j:
                            if c==1:
                                p1+=1
                            h1[i]='x'
                            h2[i]='x'
    
    for j in ['14','13','12','11','10','09','08','07','06','05','04','03','02']:
        c=0
        for x in ls:
            c+=1
            for i in range(len(h1)):
                if x[i]=='x':
                    pass
                elif x[i][1][0]==x[i][1][2] or x[i][1][2]==x[i][1][4] or x[i][1][1]==x[i][1][3]:
                    if x[i][1][2]==j:
                        if c==1:
                            p1+=1
                        h1[i]='x'
                        h2[i]='x'
                        
    for i in range(len(h1)):
        if h1[i]=='x':
            pass
        else:
            if len(set(h1[i][1]))<len(set(h2[i][1])):
                p1+=1
                h1[i]='x'
                h2[i]='x'
            elif len(set(h2[i][1]))<len(set(h1[i][1])):
                h1[i]='x'
                h2[i]='x'
            elif len(set(h2[i][1]))==3:
                print h1[i][1],h2[i][1],i
                raw=raw_input('did h1 win?.. ')
                if raw=='y':
                    p1+=1
                h1[i]='x'
                h2[i]='x'
    
    for i in range(len(h1)):
        if h1[i]=='x':
            pass
        else:
            if len(set(h1[i][1]))==4:
                a=h1[i][1][:]
                b=h2[i][1][:]
                for x in set(h1[i][1]):
                    a.remove(x)
                for x in set(h2[i][1]):
                    b.remove(x)
                if a==b:
                    print h1[i][1],h2[i][1],i
                    raw=raw_input('did h1 win?.. ')
                    if raw=='y':
                        p1+=1
                    h1[i]='x'
                    h2[i]='x'
                elif a>b:
                    p1+=1
                    h1[i]='x'
                    h2[i]='x'
                else:
                    h1[i]='x'
                    h2[i]='x'
                    
    for i in range(len(h1)):
        if h1[i]=='x':
            pass
        else:
            if h1[i][1]>h2[i][1]:
                p1+=1
                h1[i]='x'
                h2[i]='x'
            else: 
                h1[i]='x'
                h2[i]='x'
    return p1
                








        # if h1[i][0]=='Y' or h2[i][0]=='Y':
        #     if h1[i][0]=='N' or h2[i][0]=='N':
        #         if h1[i][0]=='Y':
        #             if len(set(h2[i][1]))==2:
        #                 p2+=1
        #             else:
        #                 p1+=1
        #         else:
        #             if len(set(h1[i][1]))==2:
        #                 p1+=1
        #             else:
        #                 p2+=1
                               
        #     else:
        #         if int(h1[i][1][0])-int(h1[i][1][4])==4:
        #             if int(h2[i][1][0])-int(h2[i][1][4])==4:
        #                 if h1[i][1]>h2[i][1]:
        #                     p1+=1
        #                 else:
        #                     p2+=1
        #             else:
        #                 p1+=1
        #         elif int(h2[i][1][0])-int(h2[i][1][4])==4:
        #             p2+=1
        #         elif h1[i][1]>h2[i][1]:
        #             p1+=1
        #         else:
        #             p2+=1
        # else:
        #     if len(set(h1[i][1]))==1 or len(set(h2[i][1]))==1:
        #         if len(set(h1[i][1]))==1 and len(set(h2[i][1]))==1:
        #             if h1[i][1][1]>h2[i][1][1]:
        #                 p1+=1
        #             else:
        #                 p2+=1
        #         else:
        #             if len(set(h1[i][1]))<len(set(h2[i][1])):
        #                 p1+=1
        #             else:
        #                 p2+=1
        #     elif len(set(h1[i][1]))==5 and len(set(h2[i][1]))==5:
        #         if h1[i][1]>h2[i][1]:
        #             p1+=1
        #         else: p2+=1
            
