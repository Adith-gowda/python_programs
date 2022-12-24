#Q. Write a Python Program to get a string made of the first 2 and last 2 characters from a given string.
#  If the string length is less than 2, print 'Invalid'
s_org=input()
if len(s_org)<2:
    print("invalid")
else:
    s_new=""
    s_new= s_new +s_org[0:2]+s_org[-2]+s_org[-1]
    print(s_new)

# or 
s = input("Enter string:")
if len(s)<2:
    print("invalid syntax")
else:
    s1 = s[:2]
    s2 = s[-1:-3:-1]
    s2 = s2[::-1]
    s3 = s1 + s2
print(s3)

#infinite string
s=input()
n=int(input())
infinite_str=False
while infinite_str!=True:
    s+=s
for i in s[0,n+1]:
    count_a=s.count("a")
print(count_a)

#
s=input().split()
print(s.sort(reverse=True))

#
n=int(input())
if n%2!=0:
    print("Weird")
    exit()
if n%2==0 and n in [2,3,4,5]:
    print("Not Weird")
    exit()
if n%2==0 and n in range(6,21):
    print("Weird")
    exit()
if n%2==0 and n>20:
    print("Not Weird")
    exit()



    




