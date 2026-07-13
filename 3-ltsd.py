#1.1 - list ops - ordered, mutable
num = [10,5,25,15]
num.append(30)
print("new list after append: ", num)
num.remove(30)
print("new list after remove: ", num)
num.sort()
print("new list after sort : ", num)
#.insert(index, value), .index(value), .pop(), .sort(), .reverse(), .clear(), .copy(), .count(), .extend()

#1.2 - find min/max no. in list
num = [10,5,25,15]
print("largest number in list : ", max(num), ", smallest number in list : ", min(num))

#1.3 - list generation using list comprehension
squares = [x*x for x in range(1,6)]
print("squares from 1-5 :", squares)

#1.4 - remove duplicate elements from list
num = [1,2,2,3,4,5,5]
print("list with duplicate elements : ", num)
numm = list(set(num))
print("list without duplicate elements : ", numm)

#2D list
n1 = [0,1,2]
n2 = [3,4,5]
nos = [n1,n2]
print(nos)
print(nos[0])
print(nos[1][2])

#2 - tuple ops - ordered, immutable
info = ("krish", "student", 21)
print("name : ", info[0])
print("work : ", info[1])
print("age : ", info[2])
print(info.count("krish")) #any char or num
print(info.index("student"))

#3 - set ops - unordered, mutable
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("union : ", set1 | set2)
print("intersection : ", set1 & set2)
#.add(value), .remove(value), .clear(), set1.update(set2), set1.difference(set2), .pop() - 1st element removed cuz unordered

#4 - dictionary ops - key & value pair - ordered, mutable
student = {"name" : "krish", "course" : "mca", "roll no." : 1}
print("items : ", student.items())
print("keys : ", student.keys())
print("values : ", student.values())

#for key, value in cap.items():
#print(key, value)
#.update({"key" : "value"}), .pop("key"), .clear()

#5 - dictionary generation using dictionary comprehension
squares = {x : x*x for x in range(1,6)}
print("squares from 1-5 : ", squares)