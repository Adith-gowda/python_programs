def check(s):
    if(s==s[::-1]):
        return 1
    return 0
l=input().split()
c=0
for i in l:
    if(check(i)):
        c+=1
    else:
        print(i,end=" ")
if(c==len(l)):
    print("-1")
    exit()
