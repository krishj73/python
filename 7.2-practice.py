#1 - create .txt & write content : Hey everyone ; We're learning file io ; I like java programming
with open("text.txt","w") as f:
    f.write("Hey everyone\nWe're learning file io in java")

#2 - replace java with python
with open("text.txt","r") as f:
    read = f.read()

replaced = read.replace("java","python")
print(replaced)    

with open("text.txt","w") as f:
    f.write(replaced)

#3 - find a word
word = "learning"
with open("text.txt","r") as f:
    read = f.read()
if (word in read): #read.find(word) != -1
    print(word+" letter found")
else:
    print(word+" letter not found")

#4 - find a word in which line
word = "learning"
read = True
line_no = 1
with open ("text.txt","r") as f:
    while read:
        read = f.readline()
        if (word in read):
            print(line_no)
        line_no+=1

#5 - print even nos. from a file
with open ("num.txt","w") as f:
    f.write("4,7,23,36,44")
with open ("num.txt","r") as f:
    data = f.read()
    print(data)

num = data.split(",")
print(num)
for value in num:
    if(int(value)%2==0):
        print(value)

count = 0
for value in num:
    if(int(value)%2==0):
        count+=1
print("No. of even nos. :",count)