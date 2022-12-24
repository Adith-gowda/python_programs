#
n=int(input())
tup=[]
for i in range(n):
    temp=[]
    m=int(input())
    sum=0
    for j in range(m):
        if j==0:
            temp.append(input())
            continue
        elif j%2==0:
            sum=sum+int(input())
        else:
            x=input()
    temp.append(sum)
    tup.append(tuple(temp))
print(tuple(tup))

#
import re 
text=input()
pattern=input()
regex=re.search(pattern,text,flags=re.IGNORECASE)
if regex:
    s=regex.start()
    e=regex.end()
    print("%d to %d" %(s,e))
else:
    print("Not Found")
#
N1=int(input())
N2=int(input())
S1=[]
S2=[]
for i in range(1,N1):
    items_1=int(input())
    S1.append(items_1)
    S1.sort()
for j in range(1,N2):
    items_2=int(input())
    S2.append(items_2)
    S2.sort()
S1.extend(S2)
print(S1)

#
n=int(input())
print("The factors of",n,"are:")
for i in range(1,n+1):
    if n%i==0:
        print(i)