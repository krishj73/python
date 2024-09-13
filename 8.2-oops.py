#diy
class Student:
    def __init__(self, name, marks) :
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("average marks is", sum/3)

    
student = Student("krish", [80, 85, 97])
student.avg()

#use __ before any variable/attribute/function to make it private
class Student:
    __name = "krish"

    def __intro(self):
        print("hey wassup")

    def welcome(self):
        self.__intro()

s1 = Student()
s1.welcome()

#super - used to access stuff from parent class

print("-----Welcome to the bank-----")
class Account:
    def __init__(self, bal, accno) :
        self.balance = bal
        self.accnum = accno
    
    def debit(self, amount, balance):
        if balance>0 and amount>0 and balance>amount:
            balance-=amount
            print(amount, "amount withdrawn")
            print("Balance is ", balance)

        else:
            print("Enter valid amount to withdraw")
    
    def credit (self, amount, balance):
        if amount>0:
            balance+=amount
            print(amount, "amount credited")
            print("Balance is ", balance)

        else:
            print("Enter valid amount to deposit")
        
balance = int(input("Enter balance available : "))
if balance<0 :
    print("Enter valid balance")
else:
    task = int(input("Withdraw / Deposit / Show balance (1/2/3): "))
    user = Account(balance, 1)

    if task == 1:
        amount = int(input("Enter amount to withdraw : "))
        user.debit(amount, balance)
    elif task == 2:
        amount = int(input("Enter amount to deposit : "))
        user.credit(amount, balance)
    elif task == 3:
        print("Balance is", balance)
    else:
        print("Choose valid action")