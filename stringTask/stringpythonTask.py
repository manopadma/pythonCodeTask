#1.Check binary
# def binary(str):
#     for ch in str:
#         if ch !="0" and ch!="1":
#             return False
#     return True
# number=input("Enter the String")
# if binary(number):
#     print(1)
# else:
#     print(0)

#2.rmove space
# string=input("enter the string")
# b=""
# for char in string:
#     if char!=" ":
#         b+=char
# print(b)

#3.reverse string
# d="string"
# c=""
# for char in d:
#     c=char+c
# print("The Original String:",d)
# print("The Reverse String:",c)

# 4.check String
char="string"
length=len(char)
b=True
first=char[0]
if char:
    if char!=first:
        b=False
print(b)

 
 # # 5.Removing vowels
# x=input(("enter the  String:"))
# vowels="aeiouAEIOU"
# a=""
# for y in x:
#     if y not in vowels:
#         a=a+y
# print(a)

# 6.Count camel case in given string
# a="STRing"
# upperCase=""
# for i in a:
#     if i<="A" or i<="Z":
#         upperCase=upperCase+i
# length=len(upperCase)
# print("length of the uppercase in the string",length)


#7.
# p="#STRing1234"
# lower=0
# upper=0
# special=0
# number=0
# for q in p:
#     if q>="a" or q<="z":
#         lower=lower+1
#     elif q>="A" or q<="Z":
#         upper=upper+1
#     elif q>="0" or q<="9":
#         number=number+1
#     else:
#         special=special+1
# print("length of lower case in given string is:",lower)
# print("length of lower case in given string is:",upper)
# print("length of lower case in given string is:",number)
# print("length of lower case in given string is:",special)
#Pattern of string
# ch="GeeK"
# for i in ch:

