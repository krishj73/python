#indexing
name = "krish jaisingh"
if (name[0].islower()):
    print(name.capitalize())

fname = name[0:5] #[:5]
lname = name[6:14] #[6:]
print(fname)
print(lname)

#5 - *args - when no. of arguments is unknown
def sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print("sum of numbers : ", sum(10, 20, 30, 40, 50))

#6 - **kwargs (keyword arguments)
def details(**kwargs):
    for key, value in kwargs.items():
        print(key," : ",value)
details(name = "krish", course = "mca", rollno = 1)

#*args
def add1(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add1(1,2,3))

def add2(*args):
    sum = 0
    #args[0] = 5 - error cuz its a tuple so unchangable
    args = list(args)
    args[0] = 5
    for i in args:
        sum += i
    return sum
print(add2(1,2,3))