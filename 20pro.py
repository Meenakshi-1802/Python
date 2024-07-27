#Revision
print("Hello world")
print("meenakshi is my name.")
print("my age is 21.")
print("meenakshi is my name. " ,("my age is 21"))
print(23)
print(23+35)
name = "meenakshi"
age = 21
print(name)
print(age)
print("my name is :",name)
print("my age is :",age)
age2 = age
print(age2)
print(type(name))
print(type(age))
name1 = "mp"
name2 = "mp"
name3 ='''mp'''
print(name1)
print(name2)
print(name3)
 
#qs-1
a = 2
b = 5
sum = a + b
print(sum)

#single line comment
""" this is 
a multiline 
comment """

#input
name = input("name:")
print(name)
age = input("21:")
print("my name is",name,"and i am",age,"years old")

#conditional statement
if(age >= 18):
    print("vote")
elif(age <= 18):
    print("underage")

#arithmatic
a = 2
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#Relational
a = 50
b = 20
print(a == b) #False
print(a != b) #True

#Assignment
num = 10
num = num + 10
print("num :" , num)

#logical
print(not False)
print(not True)

#Type conversion
a = 2
b = 2.34
sum = a + b
print(sum)

#Type casting
a = int("2")
b =4.45
print(type(a))
print(a + b)

#input
input("enter your name :")
print("welcome",name)

#Strings
str1 = "this is a string"
str2 = 'string'
str3 = """this is a string"""

#concatenation
str1 = "apna"
len = len(str1)
str2 = "college"
len = len(str2)
print(str1 + str2)

#indexing
str = "apna college"
ch = str[2]
print(str[2])

#slicing
str = "apna college"
print(str[1:4])

str = "i am studying python"
print(str.endswith("hon"))
print(str.capitalize())
print(str.replace("o","a"))
print(str.find("o"))
print(str.count("from"))

#List
marks = [1,2,3,4,5,6]
print(marks)
print(type(marks))
#slicing
marks = [1,2,3,4,5,6]
print(marks[2:4])
#methods
list = [1,2,3,4,5,6]
list.append(8)
print(list.append)
list = list.sort()
print(list.sort)
print(list.sort(reverse=True))
list.reverse()
list.insert(1,5)
list.remove(4)
list.pop(2)
print(list)

#Tuples
tup = (1,2,3,4)
print(tup[0])
print(tup[1])

#slicing
tup = (1,2,3,4)
print(tup[1:3])

#Methods
tup = (1,2,3,4)
print(tup.index(4))
print(tup.count(2))

#Dictionary
info = {
    "key" : "value",
    "name" : "apna college",
    "learning" : "coding",
}
print(info)

#nested
student = {
    "name" :"meenakshi",
    "subjects" : {
        "phy" : 97,
        "chem" : 94,
        "math" : 95,
    }
}
print(student)
#methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get())
print(student.update())

#sets
collection = {1,2,3,4}
print(collection)
#methods
print(set.add(5))
print(set.remove(2))
print(set.clear())
print(set.pop())

set1 = {1,2,3}
set2 = {3,4,5}
print(set.union(set2))
print(set.intersection(set2))

#Loops
count = 1
while count<=5 :
    print("hello")
    count += 1

print(count)







