#1.find minimum or maximum
print("Find Maximum or minimum in Two Numbers")
value1= int(input("enter First Value"))
value2= int(input("enter second Value"))
if(value1> value2):
    print("Value 1 is Greater than Value 2")
elif(value1<value2):
    print("Value 2 is Greater than Value 1")
elif(value1 == value2):
    print("Both Value1 and Value2 are Equal")

###2.find maximum or minimum in three value
##print("find maximum or minimum in three value")
##val1= int(input("enter First Value"))
##val2= int(input("enter second Value"))
##val3= int(input("enter Third Value"))
##if(val1> val2  and val1>val3):
##    print("Value 1 is Greater than Value 2 and value 3")
##elif(val3<val2 and val2>val1):
##    print("Value 2 is Greater than Value 1 and value 3")
##else:
##    print(" Value3 is greater")
##
###3.check given number is +ve orr -ve
##print("check given number is +ve orr -ve")
##a =  float (input("Enter the Number"))
##if a>0:
##    print("The Given Value is +ve")
##elif a<0:
##    print("The Given Value is -ve")
##else:
##    print("The Given Value is Zero")
##
##
###4.check given number is divisible by 5 and 11
##    
##print("check given number is divisible by 5 and 11")
##b = int (input("Enter the Number"))
##if ((b%5 == 0) and (b%11 == 0)):
##       print("The Given Number is Divisble by 5 and 11")
##else:
##      print("The Given number is not Divisble by 5 and 11")
##
###5.Check given number is odd or even
##print("Check given number is odd or even")
##c = int (input("Enter the Number"))
##if (c % 2==0):
##    print("The Given Number is even Number")
##else:
##    print("The  Given Number is Odd Number")
##
###6.Check the leap and Non Leap Year
##print("Check the leap and Non Leap Year")
##year = int(input("Enter The Year"))
##
##if ((year % 4 == 0) and (year% 100 !=0) or (year % 400 == 0)):
##    print("The given year is leap year")
##else:
##    print("The Given year is Non Leap Year")
##
###7.Check whether  a character is alphapet or not
##
##print("Check whether  a character is alphapet or not")
##alpha = str(input("Enter the Value"))
##
##if (alpha.isalpha()):
##    print("The Given Value is Alphapet")
##else:
##    print("The Given Value is not Alphapet")
##
###8.check vowel and consonants
##print("check vowel and consonants")
##ch = input("Enter the Characters")
##
##if ((ch == 'a') or (ch == 'e') or (ch == 'i') or  (ch == 'o')or  (ch == 'u')or (ch == 'A') or (ch == 'E') or (ch == 'I') or  (ch == 'O')or  (ch == 'U')):
##    print ("The Given Character is Vowel")
##elif (ch):
##    print("The Given Character is consonants ")
##
###9. Check the Given Textis upper or lower case
##print("Check the Given Textis upper or lower case")
##text = input("Enter the text")
##
##if (text.isupper()):
##    print("The Given Text is UpperCase")
##elif(text.islower()):
##    print("The Given Text is Lower Case")
##else:
##    print("Invalid Text ")

# 10.Print day name of Week
print("Print day name of Week")
week = int(input("Enterr the Week Number"))

if (week == 1):
    print("Monday")
elif(week ==2):
    print("Tuesday")
elif(week ==3):
    print("Wednesday")
elif(week ==4):
    print("Thursday")
elif(week ==5):
    print("Friday")
elif(week ==6):
    print("Saturday")
elif(week ==7):
    print("Sunday")
else:
    print("Invalid Input")

# 11 Find the Number days in Month
print("Find the Number days in Month")
month = int(input("Enter the month Number(1-12)"))
if (month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month == 12):
    print("This month Contain 31 days")
elif(month == 2):
    print("This month contain 28 /29 days")
elif(month == 4 or month == 6 or month == 9 or month == 11):
    print("This month contain 30 days")
else:
    print("Invalid Input")

### 12.count total number of notes in given amount

amt =int(input("Enter the amount"))
fiveHundred = 0
hundredRupe =0
fiftyRupee = 0
twentyRupee = 0
tenRupee =  0
fiveRupee = 0
twoRupee = 0
oneRupeeCoin =0

if(amt>=500):
    fiveHundred = amt//500
    amt -= fiveHundred *500
    
if(amt>=100):
    hundredRupe =amt//100
    amt-= hundredRupe*100
if(amt>=50):
    fiftyRupee =amt//50
    amt-= fiftyRupee*50
if(amt>=20):
    twentyRupee =amt//20
    amt-= twentyRupee*20
if(amt>=10):
    tenRupee =amt//10
    amt-= tenRupee*10
if(amt>=5):
    fiveRupee =amt//5
    amt-= fiveRupee*5
if(amt>=2):
    twoRupee=amt//2
    amt-= twoRupee*2
if(amt>=1):
    oneRupeeCoin =amt//1
    amt-= hundredRupe*1
print("500 Notes:",fiveHundred)
print("100 Notes:",hundredRupe)
print("50  Notes:",fiftyRupee)
print("20  Notes:",twentyRupee)
print("10  Notes:",tenRupee)
print("05  Notes:",fiveRupee)
print("02  Notes:",twoRupee)
print("01  Coins:",oneRupeeCoin)
    
# 13.Whether triangle is valid or not using angles
print("Whether triangle is valid or not using angles")
angle1 = int(input("Enter the 1st angle"))
angle2 = int(input("Enter the 2nd angle"))
angle3 = int(input("Enter the 3rd angle"))

sum = angle1 + angle2 + angle3
if (sum == 180  and angle1> 0 and angle2 > 0 and angle3>0):
    print("This Triangle is Valid")
else:
    print("This Triangle is invalid")

#14.whether triangle is valid or not using side of triangle
print("whether triangle is valid or not using side of triangle")
side1 = int(input("Enter the Side 1 for triangle"))
side2 = int(input("Enter the Side 2 for triangle"))
side3 = int(input("Enter the Side 3 for triangle"))

if((side1+side2)> side3):
    if((side2+side3)>side1):
        if ((side1+side3)>side2):
            print("This Triangle is Valid")

else:
    print("This Triangle is invalid")

#15. check the given triangle is equalateral or scalene or isosceles 
print("check the given triangle is equalateral or scalene or isosceles ")
triSide1 = int(input("Enter the side 1"))
triSide2 = int(input("Enter the side 2"))
triSide3 = int(input("Enter the side 3"))

if(triSide1 == triSide2 and triSide2 == triSide3 and triSide1 == triSide3):
    print("This Triangle is Equalateral ")
elif(triSide1 == triSide2 or triSide2 == triSide3 or triSide1 == triSide3):
    print("This triangle is isosceles ")
else:
    print("This is Scalene Triangle")

#16.check profit or loss
print("check profit or loss")
costPrice = int(input("Enter The Cost Price"))
sellingPrice = int (input("Enter The Selling Price"))
amount = 0

if(sellingPrice > costPrice):
    amount = sellingPrice-costPrice
    print(f"Profit Value is {amount}")
elif(sellingPrice < costPrice):
    amount = costPrice - sellingPrice
    print(f"Loss Value is {amount}")
else:
    print("No profit and Loss")


#17.enter student marks and find percentage and grade
print("enter student marks and find percentage and grade")
tamilMark = int(input("Enter the Tamil Mark"))
englishMark = int(input("Enter the English Mark"))
mathsMark = int(input("Enter the Maths Mark"))
sciMark = int(input("Enter the Science Mark"))
socMark = int(input("Enter the Social Mark"))
total = tamilMark+englishMark+mathsMark+sciMark+socMark
print(f"The Total Mark is {total}")
percentage = int (total/5.0)
print(f"The Percentage is {percentage}")
if(percentage>=90):
    print("Grade A")
elif(percentage>=80):
    print("Grade B")
elif(percentage>=70):
    print("Grade C")
elif(percentage>=60):
    print("Grade D")
elif(percentage>=40):
    print("Grade E")
else:
    print("Grade F")


#18.calculate gross salary of Employee
print("calculate gross salary of Employee")
basicSalary = int(input("Enter Employee Basic Salary"))

if(basicSalary<=10000):
    dailyAllowence = basicSalary+0.8
    hra= basicSalary*0.2
elif(basicSalary<=20000):
    dailyAllowence = basicSalary+0.9
    hra= basicSalary*0.25
else:
    dailyAllowence = basicSalary+9.5
    hra= basicSalary*0.3
grossSalary = basicSalary+dailyAllowence+hra
print(f"The Gross Salary of Employee is {grossSalary}")

#19
print("Quadratic Equation")
import math
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

#20
print("Calculate Electricity Bill")
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
   
#21.Check given text is character or digit or spl character
print("Check given text is character or digit or spl character")
character=input("Enter any Character")
if(character.isalpha()):
    print("The Entered character is an alphabet")
elif(character.isdigit()):
    print("The Entered character is Digit")
else:
    print("The Entered character is spl Character")












    
