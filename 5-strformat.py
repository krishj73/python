#string format
var1 = "cow"
var2 = "moon"
print("The {} jumped over the {}".format(var1, var2))
print("The {1} jumped over the {0}".format(var1, var2))
#print("The {var1} jumped over the {var2}".format(var1="dog", var2="bridge"))
#text = "The {} jumped over the {}"
#print(text.format(var1, var2))

name = "krish"
print("hey, what's up {:10} hope u doing good".format(name))
print("hey, what's up {:>10} hope u doing good".format(name))
print("hey, what's up {:<10} hope u doing good".format(name))
print("hey, what's up {:^10} hope u doing good".format(name))

pi = 3.1415
print("value of pi is {:.2f}".format(pi))
num = 1000
print("num is {:,}".format(num))
print("num is {:b}".format(num)) #binary
print("num is {:o}".format(num)) #octal
print("num is {:x}".format(num)) #hexadecimal
print("num is {:e}".format(num)) #scientific notation

#random
import random
num1 = random.randint(1,6) #random.random() - bw 0 & 1
print(num1)