###1.Display first 10 natural numbers
##for num in range(1,11):
##    print(num)
##
###2.sum of first 10 natural numbers
##
##sum=0
##for val in range(1,11):
##    sum+=val
##    print(sum)
###3.Display n terms of natural number and their sum
##
##add=0
##a=int(input("Enter the 'n' term:"))
##for i in range(1,a):
##    add+=i
##    print(add)
##
###4.read 10 numbers and find their sum and average
##addition=0
##for n in range(1,10):
##    addition+=n
##    print("Addtion of 10 Numbers",addition)
##avg=addition/10
##print("Average of 10 numbers",avg)
##
###5.Display the cube of integer
##cube=0
##for value in range(1,5):
##    cube= value*value*value
##    print("The cube Value is:",cube)
###6.Display Multiplication table
##multiplication=0
##mul=int(input("Enter the number to multiplication"))
##for table in range(1,11):
##
##    multiplication=mul*table
##    print(f"{table}*{mul}=",multiplication)
#####7.display multiplication upto numbers
##
##table1=int(input("Enter the number"))
##i=1
##j=1
##for i in range(1,table1):
##    for j in range(1,11):
##        m=i*j
##        print(f"{i}*{j}=",m)
#####8. display n terms of  odd natural number and thier sum
##
##total=0
##for oddNum in range(1,20,2):
##    print(oddNum)
##    total+=oddNum
##print("The Odd Number total",total)
####9.display a pattern like a right angle triangle using an asterisk.
astrixNum=int(input("Enter the Number:"))
for k in range(1,astrixNum+1):
    for l in range(1,astrixNum+1):
        if(l<=astrixNum-k):
            print(' ',end=" ")
                              
        else:
            print("*",end=" ")
            print()
#10.program to make such a pattern as a pyramid with an asterisk
for p in range(4):
    for q in range(4,p,-1):
        print('',end=" ")
    for s in range(p+1):
        print("*",end=" ")
    print()
