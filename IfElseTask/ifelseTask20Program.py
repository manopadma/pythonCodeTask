###check profit or loss
##
##costPrice = int(input("Enter The Cost Price"))
##sellingPrice = int (input("Enter The Selling Price"))
##amount = 0
##
##if(sellingPrice > costPrice):
##    amount = sellingPrice-costPrice
##    print(f"Profit Value is {amount}")
##elif(sellingPrice < costPrice):
##    amount = costPrice - sellingPrice
##    print(f"Loss Value is {amount}")
##else:
##    print("No profit and Loss")
##

#enter student marks and find percentage and grade

##tamilMark = int(input("Enter the Tamil Mark"))
##englishMark = int(input("Enter the English Mark"))
##mathsMark = int(input("Enter the Maths Mark"))
##sciMark = int(input("Enter the Science Mark"))
##socMark = int(input("Enter the Social Mark"))
##total = tamilMark+englishMark+mathsMark+sciMark+socMark
##print(f"The Total Mark is {total}")
##percentage = int (total/5.0)
##print(f"The Percentage is {percentage}")
##if(percentage>=90):
##    print("Grade A")
##elif(percentage>=80):
##    print("Grade B")
##elif(percentage>=70):
##    print("Grade C")
##elif(percentage>=60):
##    print("Grade D")
##elif(percentage>=40):
##    print("Grade E")
##else:
##    print("Grade F")
##    
# calculate gross salary of Employee

##basicSalary = int(input("Enter Employee Basic Salary"))
##
##if(basicSalary<=10000):
##    dailyAllowence = basicSalary+0.8
##    hra= basicSalary*0.2
##elif(basicSalary<=20000):
##    dailyAllowence = basicSalary+0.9
##    hra= basicSalary*0.25
##else:
##    dailyAllowence = basicSalary+9.5
##    hra= basicSalary*0.3
##grossSalary = basicSalary+dailyAllowence+hra
##print(f"The Gross Salary of Employee is {grossSalary}")
##
    
#find minimum or maximum

value1= int(input("enter First Value"))
value2= int(input("enter second Value"))
if(value1> value2):
    print("Value 1 is Greater than Value 2")
elif(value1<value2):
    print("Value 2 is Greater than Value 1")
elif(value1 == value2):
    print("Both Value1 and Value2 are Equal")
#find maximum or minimum in three value

val1= int(input("enter First Value"))
val2= int(input("enter second Value"))
val3= int(input("enter Third Value"))
if(val1> val2  and val1>val3):
    print("Value 1 is Greater than Value 2")
elif(val3<val2 and val2>val1):
    print("Value 2 is Greater than Value 1")
else:
    print(" Value3 is greater")

#17

a= int(input("Enter the Number:")
b= int(input("Enter the Number:")
c= int(input("Enter the Number:")
val=(b*b)-(4*a*c)

if(val>0):
    root1=(-b+sqrt(val))/(2*a)
    root2=(-b+sqrt(val))/(2*a)
    print("Root1:",root1)
    print("Root2:",root2)
elif(val==0)
    root1= root2=-b/(2*a)
    print("Root1:",root1)
    print("Root2:",root2)
else:
    root1=root2=-b/(2*a)
    i=sqrt(-val)/(2*a)
    print("Root1:",root1)
    print("Root2:",root2)
    print("Imaginary:",i)

#21
unit=int(input("Enter the Units:")
billAmt=0
if(unit<=50):
    billAmt=unit*0.5
elif(unit<=150):
    billAmt=25+((unit-50)*0.75)
elif(unit<=250):
    billAmt=62.5+((unit-150)*1.20)
else:
    billAmt=220+((unit-250)*1.50)
tax=bill*0.2
total=billAmt+tax
print("The Total Bill is {total}")
    

        
