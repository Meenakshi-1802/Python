#eval function
print(eval("5+7"))

x = eval(input("enter a data:"))
print(x,type(x))

x,y = input("enter two numbers:").split()
print(x,y)

x,y,z = input("enter a date:").split('/')
print(x,y,z)

x,y,z = [int(i) for i  in input("enter 3 numbers").split()]
print(x,y,z,type(x))

x,y,z = [eval(g) for g in input("enter 3 data:").split()]
print(x,y,z,type(x))

t1 = list([eval(g) for g in input("enter a data:").split()])
print(t1,type(t1))

t2 = tuple([eval(g) for g in input("enter a data:").split()])
print(t2,type(t2))

