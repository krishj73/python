#1
class Circle:
    pi = 3.14
    def __init__(self, r):
        self.radius = r

    def Area(self):
        area = r * r * 3.14
        print("area is", area)

    def Perimeter(self):
        per = 2 * 3.14 * r
        print("perimeter is", per)
    
r = int(input("enter radius : "))
user = Circle(r)
user.Area()
user.Perimeter()

#2
class Employee:
    def __init__(self, role, dept, salary) :
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role of employee is", self.role)
        print("Department of employee is", self.dept)
        print("Salary of employee is", self.salary)

class Eng(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 50000)

employee = Employee("Accountant", "Acc", 50000)
eng = Eng("aman", 21)
eng.showDetails()

#3
class OrderPrice:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __op__(o1, o2):
        return o1.price > o2.price
    
o1 = OrderPrice("snacks",100)
o2 = OrderPrice("drinks",200)
print(o1>o2)

#4
import random
num = random.randint(1,10)

while True:
    user = input("enter a guess or quit (Q) : ")
    if (user=="Q"):
        break

    user = int(user)
    if (user==num):
        print("Right guess! Game over")
        break
    elif (user>num):
        print("Wrong guess, maybe a lil less")
    else:
        print("Wrong guess, maybe a lil higher")


#5
import random
import string

pass_len = 8
str = string.ascii_letters + string.digits + string.punctuation

#password = ""
#for i in range(pass_len):
#    password += random.choice(str)

#list comprehension method
password = "".join( [random.choice(str)] for i in range(pass_len) )
print("your password is", password)