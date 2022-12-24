a=input()
s="";s1=""
l=[int(input()) for i in range(0,len(a))]
for i in range(1,len(a)+1):
    for j in range(0,len(a)):
        if(l[j]==i):
            s1+=str(j+1)
            s+=a[j]
print(s)
for i in range(0,len(s1)): print(s1[i])
