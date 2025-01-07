#if/else
age = int(input("Enter user age : "))
if age<18:
    print("Chhoti bacchi ho kya")
elif age==18:
    print("Ab majaa ayega na bhidu")
else:
    print("Tu toh bada ho gaya")

#nested if/else
a=10
b=20
c=30
if a>b:
    if a>c:
        greatest = a
    else:
        greatest = c
else:
    if b>c:
        greatest = b
    else:
        greatest = c

print("Greatest number :",greatest)