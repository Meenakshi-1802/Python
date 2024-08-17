#while loop
x = 5
while x < 10:
    print("hello")
    x = x+1
x = 10
while x > 1:
    print("hello")
    x = x-1

x = int(input("enter first number:"))
y = int(input("enter second number:"))
z = int(input("enter third number:"))

if x > y and x > z:
    print(x,"is greater")

elif y > x and y > z:
    print(y,"is greater")

elif z > x and z > y:
    print(z,"is greater")

