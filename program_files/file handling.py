f=open("file1.txt","w+") # to write in a file 
for i in range(10):
    f.write("This is line %d\r\n" %(1+i))
    print(i)
f.close()

f=open("file1.txt","a+") #to append into a file 
for i in range(2):
    f.write("appended line %d\r\n" %(i+1))
    print(i)
f.close()

f=open("file1.txt",) #by default the mode is read 
if f.mode=="r":
    contents=f.read()
    print(contents)
f.close()

#reading line by line 
def main():
    f=open("file1.txt","r")
    f1=f.readlines()
    for x in f1:
        print(x)
    f.close()
if __name__ == "__main()__":
    main()

def main():
    f=open("File1.txt")
    f1=f.readlines() #f.readline would only read the first line,returns a string whereas f.readlines(),returns a list, will read all of the lines
    print(f1)
    f.close()
    #for i in f1:
     #   print(i)
main()

#creating a new file 
def main():
    f=open("file2.txt","w+")
    for i in range(5):
        f.write("This is line %d\r\n" %(1+i))
        print(i)
f.close()
main()

#
def main():
    f=open("file2.txt","r")
    if f.mode=="r":
        contents=f.read()
        print(contents)
    f.close()
main()

#f=open("file3.txt","x")
#f.close()
#cursor positioning
#f=open("file3.txt","rb+") #reading and writing a binary file 
#f.write(b"0123456789abcdef")
#f.seek(5) #go to the 6 th byte in the file 
#f1=f.read(1)
#print(f1)
#f.seek(-3,2)
#f2=f.read(1)
#print(f2)
#f.close()

#
#with open(r'file3.txt',"r+") as fp:
    #fp.seek(0,2)
    #print("file handle at:",fp.tell())
    #print(fp.write("adith"))

#turncating a file 

file=open("myfile.txt","w")
file.write("hello")
file.close()

file=open("myfile.txt","a")
file.truncate()
file.close()

import os
os.rename("file1.txt","ourfile.txt")

