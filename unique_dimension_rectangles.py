n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
print(c//2)
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j==n:
            print(i,j)
    
