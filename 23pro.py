#Revision
#ques-1
number = int(input("enter a number: "))

if number >= 0:
    print("the number is positive")
else:
    print("the number is negative")

#ques-2
for i in range(1,11):
    print("i,python")

#ques-3
list = [1,2,3,4,5,6]
fruits = ["apple","banana","kiwi"]
for i in list:
    print(i)
for i in fruits:
    print(i)

#ques-4
i = 2
while i < 101:
    print(i)
    i += 2

#conversion
x = 11 # int
y = 2.88 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))

