#dictionary
#how to take input from user 
n = int(input())
dictionary=dict() #or ={}
for i in range(n):
    state=input()
    districts=int(input())
dictionary[state]=districts
#or 
dictionary.update({state:districts})
#or 
dic_to_be_appended={state:districts}
dictionary.update(dic_to_be_appended)
print(dictionary)

#how to iterate through dictionary 
for key in dictionary:
    print(key,dictionary[key])

#how to invert the items in  dictionary 
dict={}
dict1={}
for key in dict:
    values=dict[key]
    dict1[values]=key

#how to map two lists into dict
keys=[]
values=[]
newdict=dict(zip(key,values))
print(newdict)

#sets /creating an empty set 
newset=set()

#how to take inputs from user 
n=int(input())
set1=set()
for i in range(n):
    ele=input()
    set1.add(ele)
print(set1)



