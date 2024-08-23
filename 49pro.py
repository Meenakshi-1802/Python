#exception handeling
print("hii")
x = int(input("enter first number:"))
y = int(input("enter second number:"))
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("why you are dividing with zero")
print("bye")

print("hii")
x = input("enter first number:")
y = int(input("enter second number:"))
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("why you are dividing with zero")
except TypeError:
    print("error")
print("bye")

#we can write two classes at a same line:
print("hii")
x = input("enter first number:")
y = int(input("enter second number:"))
try:
    z = x/y
    print(z)
except(ZeroDivisionError,TypeError):
    print("error")
    print("bye")

print("hii")
x = input("enter first number:")
y = int(input("enter second number:"))
try:
    z = x/y
    print(z)
except:   #if we dont use the class 
    print("error")
print("bye")

cb = 10000
wb = int(input("enter amount:"))
try:
    if (cb < wb):
        raise ValueError()
    cb = cb - wb
    print("money sent")
    print("current bal is ",cb)
except ValueError:
    print("insufficient balance.")
    print("current balance is",cb)

cb = 10000
while True:
    wb = int(input("enter amount:"))
try:
    if (cb < wb):
        raise ValueError()
    cb = cb - wb
    print("money sent")
    print("current bal is ",cb)
except ValueError:
    print("insufficient balance.")
    print("current balance is",cb)

print("hii")
x = input("enter first number:")
y = int(input("enter second number:"))
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("error")
finally:
    print("bye")

print("hii")
x = int(input("enter first number:"))
y = int(input("enter second number:"))
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("error")
else:
    print("hello")
finally:
    print("bye")
















