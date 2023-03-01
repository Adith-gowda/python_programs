n=int(input())
l=[input() for i in range(n)]
l1=[]
for i in l:
    for j in range(0,len(i)):
        l1.append(i[j])
max1=-1;max1c=""
for i in range(len(l1)):
    if(l1.count(l1[i])>max1):
        max1=l1.count(l1[i])
        max1c=l1[i]
print(max1c)
        
