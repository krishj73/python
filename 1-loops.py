#for
print("for loop : ")
for i in range(0,11):
    print(i, end=" ")
print()

#while
print("while loop : ")
i=0
while(i<11):
    print(i, end=" ")
    i+=1
print()

#do while
i=0
while True:
    print(i, end=" ")
    i+=1
    if (i>10):
        break