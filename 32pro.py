#conditional statements
x = 5
if x>0:
    print(x,"is positive")
else:
    print(x,"is negative")

#find maximum of 2 numbers
p = int(input("enter first number:"))
s = int(input("enter second number:"))
if p>s:
    print(p,"is greater")
elif s>p:
    print(s,"is greater")
else:
    print("both values are same")