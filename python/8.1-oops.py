#1 - basic
class Student1:
    name = "krish"
student = Student1()
print(student.name)

# __init__(): constructor executed by default when object of class created
class Student2:
    name = "krish"
    def __init__(self): #self refers to the object created, gives location where stored when printed (self and obj same location)
        print("just creating object of class auto executes init function")
student = Student2()

class Student3:
    def __init__(self, fname):
        self.name = fname
        print("just creating object of class auto executes init function")
student = Student3 ("krish")
print(student.name)

#diy
class Student4:
    def __init__(self, fname, marks):
        print("just creating object of class auto executes init function")
        self.name = fname
        self.grade = marks
student1 = Student4("krish", 97)
print(student1.name, student1.grade)

#data of object different from data of another object is instance attribute; declared everytime
#data of object same as data of another object is class attribute; declared once

#methods (functions belonging to objects)

class Student:
    def __init__(self, fname, marks):
        self.name = fname
        self.grade  = marks
    def welcome(self):
        print("hey",self.name)
    def marks(self):
            return self.marks

student = Student("krish",97)
student.welcome()
student.marks()