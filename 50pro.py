#(1)
print("Hello,World!")

#(2)
x = 10
print(x)

#(3)
name = "Meenakshi"
print("Hello",name)

#(4)
x = 7
y = 5
z = x + y
print("sum is",z)

#(5)
remainder = 17 % 3
print(remainder)

#(6)
x = int(input("enter a number:"))
if x % 2 == 0:
    print("it is even")
#else:
    print("it is odd")

#(7)
celsius =int(input("enter temp in celsius:"))
fahrenheit = (celsius* 9/5) + 32
print("celsius to fahrenheit is",fahrenheit) 

#(8)
x = int(input("enter a number:"))
if x > 0:
    print(x,"is Positive")
elif x < 0:
    print(x,"is Negative")
else:
    print(x,"is zero")

#(9)
x = int(input("enter first number:"))
y = int(input("enter second number:"))
print("x",x,"  y",y,sep ="")

#temp = x
x = y
y = temp

print("after swapping")
print("x",x,"  y",y,sep ="")

#(10)
num = float(input("enter a number:"))
srt = num*num
print("the srt of ",num ,"is",srt)



