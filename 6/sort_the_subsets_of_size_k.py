n,k=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
s=[];t=[]
for i in range(0,n,k):
    t=l[i:i+k]
    t.sort()
    s.extend(t)
for i in s:
    print(i,end=" ")
