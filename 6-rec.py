#1 - length of list
cities = ["mumbai", "delhi", "pune", "chennai"]
def lenlist(list):
    print(len(list))
lenlist(cities)

#2 - print list items in 1 line
nos = [1,2,3,4]
def items(list):
    for i in list:
        print(i,end=" ")
items(nos)
print()

#3 - factorial
num = int(input("enter a no. : "))
def facto(num):
    fact = 1
    for i in range (1, num+1):
        fact*=i
    print("factorial is ",fact)
facto(num)

#4 - usd to inr
usd = float(input("enter usd amount : "))
def convert(usd):
    inr = usd*83
    print(usd,"usd = ",inr,"inr")
convert(usd)

#5 - odd & even
num1 = int(input("enter a no. : "))
def oddeven(num):
    if num1%2==0:
        print("even no. hai")
    else:
        print("odd no. hai")
oddeven(num1)

##recursion
#1 - print 5 nos.
def show(num2):
    if(num2==0):
        return
    print(num2,end=" ")
    show(num2-1)
show(5)
print()

#2 - factorial
#ex: num = 5, go from 5 to 1
#[5! = 4! * 5] fact(num) = fact(num-1)*n
num3 = int(input("enter a no. : "))
def fact(num3):
    if (num3==1):
        return 1
    else:
        return fact(num3-1)*num3
print(fact(num3))

#3 - sum of 1st n nos.
num4 = int(input("enter a no. : "))
def sum(num4):
    if (num4==0):
        return 0
    return sum(num4-1) + num4
print(sum(num4))

#4 - print list elements
def listo(list, idx=0):
    if (idx==len(list)):
        return
    print(list[idx],end=", ")
    listo(list, idx+1)

cities = ["mumbai", "delhi", "pune"]
listo(cities)