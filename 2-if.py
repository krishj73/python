#if/else
age = int(input("Enter user age : "))
if age<18:
    print("Chhoti bacchi ho kya")       #you're not an adult
elif age==18:
    print("Ab majaa ayega na bhidu")    #you're an adult
else:
    print("Tu toh bada ho gaya")        #you're more than an adult

a, b, c = 10, 20, 30
if a>b and a>c:
    greatest = a
elif b>a and b>c:
    greatest = b
else:
    greatest = c

print("Greatest number :", greatest)

#nested if/else
ntn = input("enter nationality : ")
age = int(input("enter age : "))

if ntn.lower() == "indian":
    if age > 18:
        print("you're eligible to vote in india")
    else:
        print("you're inelegible to vote in india")
else:
    print("you're not an indian citizen")