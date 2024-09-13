#program at operate on complex nos. (just tp not that imp)
# __add__ , __sub__ , __mul__ , __div__ , __mod__
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real,"i +", self.img, "j")

    def __add__(num1, num2):
        real = num1.real + num2.real
        img = num1.img + num2.img
        return Complex(real, img)

num1 = Complex(1, 2)
num1.showNum()
num2 = Complex(3, 4)
num2.showNum()

num3 = num1 + num2
num3.showNum()