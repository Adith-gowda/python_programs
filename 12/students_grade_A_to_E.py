n=int(input())
l=[(input().split()) for i in range(n)]
l1=[]
for i in l:
    l1.append(int(i[1]))
l1.sort()
for i in l:
    if(int(i[1])>=(l1[int(0.8*n)])):
        i[1]="A"
    elif(int(i[1])>=(l1[int(0.6*n)])):
        i[1]="B"
    elif(int(i[1])>=(l1[int(0.4*n)])):
        i[1]="C"
    elif(int(i[1])>=(l1[int(0.2*n)])):
        i[1]="D"
    else:
        i[1]="E"
for i in l:
    print(i[0]+":"+i[1])
