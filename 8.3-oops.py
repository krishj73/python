#static methods
class Intro:
    @staticmethod
    def intro():
        print("hello")
intro = Intro()
intro.intro()

#class methods
class Student:
   name = "anonymous"
   def intro (self, name):
       self.name = name
       print(self.name)

s = Student()
s.intro("krish")
print(Student.name)

#class var name & object var name are different here. to modify class var via object functions, class methods r used
class Student:
   name = "anonymous"
   def intro (self, name):
       Student.name = name #
       self.__class__.name = name #
       print(self.name)

#better way
s = Student()
s.intro("krish")
print(Student.name)

class Student:
   name = "anonymous"
   @classmethod
   def intro(cls, name):
       cls.name = name
       print(cls.name)

s = Student()
s.intro("krish")
print(Student.name)

# @property - used to declare function as attribute of object. so if any var change of function later, var related methods auto-updated
class Student:
    def __init__(self, phy, chem, mts):
        self.phy = phy
        self.chem = chem
        self.mts = mts

    @property
    def percent(self):
        return str((self.phy + self.chem + self.mts) / 3) + "%"
    
student = Student (80, 89, 97)
print(student.percent)

student.phy = 85
print(student.percent)