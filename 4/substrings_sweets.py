def sub(a,k):
    c=0;count=0
    for i in range(len(a) + 1):
        for j in range(i):
            c=0
            for h in (a[j:i]):
                if h in ['a','e','i','o','u']:
                    c+=1
            if(c==k):
                count+=1
    print(count)
a=input()
k=int(input())
sub(a,k)
