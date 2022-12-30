"""Time in Heaven
In the usual time-system, we have two time-formats: 24-hour format and the 12-hour format. 08:00:00 (hours:minutes:seconds) in the 24-hour format is written as 8:00:00 A.M in the 12-hour format. 17:25:32 in the 24-hour format is written as 05:25:32 P.M. 00:00:00 in the 24-hour format is written as 12:00:00 midnight. 12:00:00 in the 24-hour format is referred as 12:00:00 noon.

In a place called `Heaven’, the people follow an eight-hour format.

(i) 00:00:00 in the 24-hour format is written as 08:00:00 midnight.

(ii) Time in the range, from 00:00:01 hours to 07:59:59 in the 24-hour format is written as the same time with a suffix A.M. For eg: 07:00:10 in the 24-hour format is written as 07:00:10 A.M. in the 8-hour format.

(iii) 08:00:00 in the 24-hour format is written as 08:00:00 midmorning.

(iv) Time in the range, from 08:00:01 to 15:59:59, in the 24-hour format is written as the time in the range, from 00:00:01 to 07:59:59 , with a suffix B.M. For eg., 09:11:13 in the 24-hour format is written as 01:11:13 B.M .

(v) 16:00:00 in the 24-hour format is written as 08:00:00 midevening.

(vi)Time in the range, from 16:00:01 to 23:59:59 in the 24-hour format is written as the time in the range from 00:00:01 to 07:59:59, with a suffix C.M. For e.g., 17:59:59 in 24-hour format is written as 01:59:59 C.M

Given the time in the 12-hour format, Write an algorithm and the subsequent code to convert the given time into the time in `Heaven’ (ie., in to an 8-hour format)

Input format :

Time in the 12-hour format, hh:mm:ss followed by A.M or P.M or midnight

Output format :

Time in the 8-hour format, hh:mm:ss followed by A.M or B.M or C.M or midnight or midmorning

Illustration :

Input

12:00:00 midnight

Output

08:00:00 midnight

Input

02:00:11 P.M

Output:

06:00:11 B.M"""

l=input().split(" ")
l.extend(l[0].split(":"))
del l[0]

if(l[0]=="P.M"): l[1]=str(int(l[1])+12)
elif(l[0]=="midnight"): l[1]="00"
elif(l[0]=="noon"): l[1]="12"

if(int(l[1])==0 and int(l[2])==0 and int(l[3])==0): print("08:00:00 midnight")
elif(int(l[1])==8 and int(l[2])==0 and int(l[3])==0): print("08:00:00 midmorning")
elif(int(l[1])==16 and int(l[2])==0 and int(l[3])==0): print("08:00:00 midevening")
elif(int(l[1])>=0 and int(l[1])<=7): print(l[1]+":"+l[2]+":"+l[3]+" "+"A.M")
elif(int(l[1])>=8 and int(l[1])<=15): print("0"+str(int(l[1])-8)+":"+l[2]+":"+l[3]+" "+"B.M")
elif(int(l[1])>=16 and int(l[1])<=23): print("0"+str(int(l[1])-16)+":"+l[2]+":"+l[3]+" "+"C.M")

