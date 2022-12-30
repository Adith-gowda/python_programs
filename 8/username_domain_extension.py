l=input().split("@")
l.extend(l[1].split("."))
del l[1]
for i in range(0,len(l)):
    print(l[len(l)-i-1])
