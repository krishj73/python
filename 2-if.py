#if/else
age = int(input("Enter user age : "))
if age<18:
    print("Chhoti bacchi ho kya")
elif age==18:
    print("Ab majaa ayega na bhidu")
else:
    print("Tu toh bada ho gaya")

#nested if/else
a, b, c = 10, 20, 30

if a>b and a>c:
    greatest = a
elif b>a and b>c:
    greatest = b
else:
    greatest = c

print("Greatest number :", greatest)