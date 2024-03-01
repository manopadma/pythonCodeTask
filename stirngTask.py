#print alphaber ,number, special character from given string
##a="**decoding123456789everyday##"
##s1=""
##s2=""
##s3=""
##for ch in a:
##    if ch.isalpha():
##        s1+=ch
##    elif ch.isdigit():
##        s2+=ch
##    else:
##        s3+=ch
##print("s1:",s1)
##print("s2:",s2)
##print("s3:",s3)

#Reverse the Given String

b="string"
c=""
for char in b:
    c=char+c
print("The Original String:",b)
print("The Reverse String:",c)

a="**decoding123456789everyday##"
s1=""
s2=""
s3=""
for ch in a:
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        s1+=ch
    elif (ch>='0' or ch<='9'):
        s2+=ch
    else:
        s3+=ch
print("s1:",s1)
print("s2:",s2)
print("s3:",s3)

amt=int(input("Enter the Amount:"))
twoThousand=0
fiveHundred=0
hundred=0
fifty =0
twenty=0
