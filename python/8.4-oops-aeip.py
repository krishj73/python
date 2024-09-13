#abstraction - hiding class implementation details from user & shown only imp things
#encapsulation - keeping data & functions in 1 unit (object)

#inheritance - when 1 class (child) derives properties & methods of another class (parent)
#since class mercedez is sub-class of class car, it can use functions of class car

#1. single inheritance - parent class ==> child classs
class Car:
    @staticmethod
    def start():
        print("car started...")

class Mercedez(Car):
    def __init__(self, name) :
        self.name = name

car = Mercedez("AMG")
car.start()

#2. multiple inheritance - parent class 1 & parent class 2 ==> child class
class A:
    a = "welcome to class A"
class B:
    b = "welcome to class B"
class C (A, B):
    c = "welcome to class C"

c = C()
print(c.a)
print(c.b)

#3. multilevel inheritance - parent class ==> sub-parent class ==> child class
class A:
    a = ("welcome to class A")
class B (A):
    b = ("welcome to class B")
class C (B):
    c = ("welcome to class C")

c = C()
print(c.a)
print(c.b)

#polymorphism
#operator overloading - using operators in diff ways
print(1+2)
print("hello"+"brother")