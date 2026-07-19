#user-defined functions
#1.1 - function with arguments & return
x = int(input("enter number 1 : "))
y = int(input("enter number 2 : "))
def add(num1, num2):
    return num1+num2
print("sum is ", add(x,y))

#1.2 - function returning multiple values
def func(nums):
    add = sum(nums)
    avg = add / len(nums)
    return add, avg
nums = [1,2,3,4,5]
sum, average = func(nums)
print("sum : ", sum, ", average : ", average)

#2 - factorial
num = int(input("enter number to find factorial : "))
def fact():
    fact = 2
    for i in range(3, num+1):
        fact *= i
    return fact
print(f"factorial of {num} : ", fact())

#3 - prime or composite
num = int(input("enter a number to find if its prime / composite : "))
def pc():
    isPrime = True
    if num < 2:
        print("number is neither prime nor composite")
    else:
        for i in range(2, int(num**0.5)):
            if num % i == 0:
                isPrime = False
                break
            else:
                return isPrime
    if isPrime:
        print(f"the number {num} is prime")
    else:
        print(f"the number {num} is composite")
pc()

#4.1 - lambda - anonymous function
sq = lambda x : x*x
print("square of number 5 : ", sq(5))

#4.2 - lambda with filter()
num = [1,2,3,4,5,6]
even = list(filter(lambda x : x % 2 == 0, num))
print("even numbers : ", even)