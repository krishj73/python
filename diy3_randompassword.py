import random
import string

print("Welcome to our Random Password Generator")

def main():
    length=int(input("Enter desired password length :"))
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digit=string.digits
    symbol=string.punctuation
    combine=lower+upper+digit+symbol
    
    x=random.sample(combine, length)
    password="".join(x)

    print(password)
    main()
main()