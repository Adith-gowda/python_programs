n,k=map(int,input().split())
l=list(map(int,input().split()))
t=[];m=[]
for i in range(0,n,k):
    t=l[i:i+k]
    t.sort(reverse=True)
    m.extend(t)
for i in m: print(i,end=" ")
