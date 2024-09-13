#indexing
name = "krish jaisingh"
if (name[0].islower()):
    print(name.capitalize())

fname = name[0:5] #[:5]
lname = name[6:14] #[6:]
print(fname)
print(lname)

#*args - to pass many parameters at once & **kwargs
def add1(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(add1(1,2,3))

def add2(*args):
    sum = 0
    #args[0] = 5 - error cuz its a tuple so unchangable
    args = list(args)
    args[0] = 5
    for i in args:
        sum+=i
    return sum
print(add2(1,2,3))