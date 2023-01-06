k=int(input())
sum2=1;h=0
for i in range(2,k+1):
    if(sum2==k):
        h=i-1
        break
    sum2*=i
if(h==0):
    print("-1")
    exit()
sum1=1
if h%2==0:
    i=2
    while i<=h:
        sum1=sum1*i
        i+=2
    print(sum1)
    exit()
else:
    i=1
    while i<=h:
        sum1*=i
        i+=2
    print(sum1)
    exit()
