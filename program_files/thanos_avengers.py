in_s,n=input().split()
l=[];flags=False
for i in range(int(n)):
    xi,yi=input().split()
    l.append((int(xi),int(yi)))
for i in l:
    if int(in_s)>i[0]:
        in_s=int(in_s)+i[1]
        flags=True
    else:
        flags=False
if flags:
    print("YES")
else:
    print("NO")
    
