s=input()
maxcount=max([s.count(i) for i in s])
for i in s: 
    if s.count(i)==maxcount : print(i,end="")
