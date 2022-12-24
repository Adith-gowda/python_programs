#function with arguement 
a=input()
def fun(a): #function header
    print("hi..."+a+"...godd morning") #function body
fun(a)#fucntion call / invoking 

#function with return 
num=int(input())
def abs_val(num):
    if num>=0:
        return num
    else:
        return -num
print(abs_val(num)) # a=abs_val(num) ; print(a)

#funtion where we are calling the collections
def changeme(mylist1):
    mylist=[1,2,3,4]
    print("values inside:",mylist)
    return(mylist)
mylist=[10,20,30]
changeme(mylist)
print("values outside:",mylist)

#example / function with multiple arguements 
x=int(input())
y=int(input())
def times1(x,y): #formal parameter 
    return(x*y)
a=times1(x,y) #actual parameter
print(a)

#required arguement or called positional arguement
str1=input()
def printme(str1):
    print(str1)
    #return(str1)
printme(str1)

#keyword arguement 
str1=input()
def printme(str1):
    print(str1)
    #return(str1)
printme(str1='string')

#example no need of maintaining the order of the actual parameter since we are using keyword arguements
def printinfo(name , age=25): #age is defualt parameter , assigning should be done from right to left
    print("name:",name)
    print("age:",age)
    return
printinfo(age=20, name="adith")
printinfo(name="dharshan")

#we cant swap the actual arguements when there is both defualt and keyword arguements
def f(a,b=2,c=3):
    print(a,b,c)
    return
f(1)
f(7,8)
f(9,c=3)

#variable-lenght arguement 
def f1(arg1,*vartuple):
    #print("the ouput is:")
    print("arg1:",arg1)
    for var in vartuple:
        print(var)
    return
f1(10)
f1(50,60,70)

#arbitrary key arguement / it forms a dictionary 
def my_function(**kid):
    print("his last name is ",kid["age"])
my_function(fname="tobias",lname="adith",age=20)#key must be a string in this case 
#both 
def f(*arg,**key1):
    print(arg , key1)
print(f(1,2,3))#double ** should be called in the last

#code 
a=5
if a%2==0:
    def func1():
        print('even')
else:
    def func1():
        print('odd')
func1()
#lambda function 
sum=lambda arg1,arg2: arg1+arg2
print("value of total:",sum(10,20))
print("value of total:",sum(20,30))

#
def one():
    print("one")
def two():
    print('two')
def three():
    print("three")
a = int(input())
if a==1:
    call_func=one
elif a==2:
    call_func=two
elif a==3:
    call_func=three
else: 
    print("invalid input")
call_func()

#variable scopes / nested functions 
x=99
def f1():
    x=88
    print("local1:",x)
    def f2():
        print("local2:",x)
    f2()
print("global in def :",x)
f1()
print("global out of def :",x)    

#recursive functions 
n=int(input())
def rfunc(n):
    print(n)
    if n>0: #recursive case 
        rfunc(n-1)
rfunc(n)

#finding factorial  of a number
def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
num=3
print("the factorial of ",num,"is :",factorial(sum))