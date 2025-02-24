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
#i=0
#while True:
#    print(i, end=" ")
#    i+=1
#    if (i>10):
#        break
#print()

print("patterns using loop : ")
#1
n=5
for i in range(1, n+1):
    print("*"*i)
print()

#2
n=5
for i in range(n, 0, -1):
    print("*"*i)
print()

#3
n=5
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
print()
#loop executed from 1 to n+1 (n)
#[' ' x (n-i)] determines no. of spaces each side, n is constant and i is inc value
#['*' x (2i - 1) ] determines no. of stars printed, ex:2x1-1 = 1 star printed, 2x2-1 = 3 stars printed

#4
n=5
#upper part
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))
#lower part
for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))
print()

#5 - square
n=5
for i in range(n):
    print('*'*n)