n=int(input())
weight_n=[];weight_m=[]
for i in range(n):
    num=int(input())
    weight_n.append(num)
m=int(input())
for j in range(m):
    num1=int(input())
    weight_m.append(num1)
total_n=sum(weight_n);total_m=sum(weight_m)
print(weight_n)
print(weight_m)
if 200+total_n-total_m<=800:
    print("Can be operated")
else:
    print("Cannot be operated")