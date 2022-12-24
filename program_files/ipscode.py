a1=str(input())
a2=str(input())
a3=str(input())
r1=[]
r2=[]
r3=[]
r4=[]
r4=list(a1)+list(a2)+list(a3)
for i in a1:
    if i in a2 and i in a3:
        r1.append(i)
    elif i in a2 and i not in a3:
        r2.append(i)
    elif i not in a2 and i not in a3:
        r3.append(i)
r1=list(set(r1))
r2=list(set(r2))
r3=list(set(r3))
r4=list(set(r4))
r1.sort()
r2.sort()
r3.sort()
r4.sort()
print(r1)
print(r2)
print(r3)
print(r4)
