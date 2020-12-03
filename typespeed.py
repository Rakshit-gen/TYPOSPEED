import time
import random
aqw=0
print('WELCOME TO TYPING PRACTICE SIMULATOR')
print('GO TO FULL SCREEN FOR BETTER VIEW')
y=input('Please enter your name')
klk=0
p,wr=[],[]
tm=[]
while aqw>-1:
    i=[]
    s=random.randint(3,15)
    for m in range(s):
        i.append(chr(random.randint(65,90)))
    i=''.join(i)
    print(i)
    klk=klk+s
    start=time.time()
    k=input('Type here')
    if k==i:
        print('Right word')
        p.append('right')
        aqw+=1
        end=time.time()
        tm.append(end-start)
        print('You answered in',end-start,'seconds')
        
        time.sleep(5)
        it=input('Do you want to continue (Y/N)')
        if it=='Y':
            pass
        elif it=='N':
            break
        k=''
    else:
        print('Wrong word')
        aqw+=1
        wr.append('0')
        k=''
    k=''
kw=0
acc=len(p)/aqw
for s in range(len(tm)):
    kw=kw+int(tm[s])
    avgt=kw/len(p)
k=''
if acc<=1:
    h='Excellent'
if 0.8<=acc<1:
    h='V.Good'
if 0.6<acc<=0.8:
    h='Good'
if 0.4<acc<=0.6:
    h='Can do better'
if 0.1<acc<=0.4:
    h='Try to practice More'
if acc<0.1:
    h='Poor'
if avgt<=3:
    timew='Excellent'
if 3<avgt<=5:
    timew='V.good'
if 5<avgt<=8:
    timew='Nice'
if 8<avgt<=12:
    timew='Can do better'
if 12<=avgt<=15:
    timew='Slow'
if 15<=avgt<=20:
    timew='Very slow'
if avgt>20:
    timew='Very poor'
kop=klk//aqw
print('Your Name',y)
print('Your Accuracy',acc)
print('Your Avg Time',avgt)
print('Average word Length',kop)
print('Right Answers',len(p))
print('Wrong Answers',len(wr))
print('Time Management',timew)
print('Remark',h)
        
