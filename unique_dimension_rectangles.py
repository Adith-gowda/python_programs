"""Unique Dimension Rectangles (UDRs)
A collection of rectangles are said to be unique dimension rectangles (UDRs) if they have distict dimensions. Dimension of a rectangle is a pair of length and breadth represented as (length, breadth). That is a collection of five rectangles with integer dimensions (10, 20), (34, 56), (12, 13), (19,10), (16, 18) are UDRs and whereas the five rectangles with the dimension (10, 20), (34, 56), (12, 13), (19,10), (20, 10) cannot be UDRs since (10, 20) and (20,10) are duplicated except change in order. Given an integer 'n' write a code to findout the number of UDRs that can be formed with area as 'n' and also print the dimensions.

For example if 168 is given then there are eight UDRs with dimensions as follows (1,168), (2, 84), (3, 56), (4,42), (6, 28), (7, 24), (8,21), (12,14).

Input Format

First line contains an integer, n

Output Format

First line contains the number of UDRs that can be formed, u

Next ‘u’ lines contains the pair of numbers in ascending order separated by a space and that can be dimension of rectangles whose area is n """

#SOLUTION :

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
print(c//2)
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j==n:
            print(i,j)
    
