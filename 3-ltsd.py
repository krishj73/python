#list - ordered & changeable
food = ["pizza", "burger", "pasta"] 
food.insert(0,"cake")               
food.index("pizza")
food.append("ice-cream")
food.remove("ice-cream")
food.pop()
food.sort()
food.reverse()
food.clear()
#copy, count, extend

#2D list
n1 = [0,1,2]
n2 = [3,4,5]
nos = [n1,n2]
print(nos)
print(nos[0])
print(nos[1][2])

#tuples - ordered & unchangable
info = ("krish", "student", 21)
print(info.count("krish")) #any char or num
print(info.index("student"))

#sets - unordered & unindexed
num1 = {1,2,3}
num2 = {4,5,6}
num1.add(7)
num1.remove(7)
num1.pop() #removes 1st element since unindexed
num1.clear()

num1.update(num2)
print(num1)
num3 = num1.union(num2)
print(num3)
num4 = num1.copy()
print(num4)
print(num1.difference(num2))
print(num1.intersection(num2))

#dictionaries - unordered & changable (key & value shit)
cap = {"india" : "new delhi", "usa" : "washington dc"}
print(cap.keys())
print(cap.values())
print(cap.items())
#for key, value in cap.items():
#print(key, value)
cap.update({"uk":"london"}) #add & update new & existing keys/values
cap.pop("uk")
cap.clear()
print(cap.items())
