#function
#creating a function
def my_function ():
    print("hello from a function")
my_function() #calling a function

#arguments
def my_function (fname):
  print(fname + "refsnes")
my_function("emil")
my_function("tobias")
my_function("linus")

#number of arguments
#this function expects 2 arguments and gets 2 arguments:
def my_function(fname, lname):
   print(fname + "  " + lname)
my_function("emil","refsnes")

#arbitrary arguments *args
#if the number of arguments is unknown,add a *before the parameter name:
def my_function(*kids):
   print("the youngest child is" +" "+kids[2])
my_function("emil","tobias","linus")

#keyword arguments
def my_function(child3,child2,child1): #this way the order of the arguments does not matter
   print("the youngest child is" + " " + child2)
my_function(child1 = "emil",child2 = "tobias",child3 = "linus")

#arbitrary keyword arguments **kwargs
#if the number of keyword arguments is unknown,add a double ** before the parameter name:
def my_function(**kid):
   print("his last name is" + " " + kid["lname"])
my_function(fname =  "tobias",lname = "refsnes")

#default parameter value
#if we call the function without argument it uses the default value:
def my_function(country = "norway"):
   print("i am from" + " " + country)
my_function("sweden")
my_function("india")
my_function()
my_function("brazil")

#passing a list as an argument
#if we send a list as an argument,it will still be a list when it reaches the function:
def my_function(food):
   for x in food:
      print(x)
fruits = ["apple","banana","cherry"]
my_function(fruits)

#return values
def my_function(x):
   return 5* x
print(my_function(3))
print(my_function(4))
print(my_function(5))
print(my_function(6))

#the pass statement:
def my_function():
   pass

#positional only arguments
def my_function(x,/):
   print(x)
my_function(3)

#keyword only arguments
def my_function(*,x): #add * before the arguments
   print(x)
my_function(x = 3)

#combine positional only and keyword only 
def my_function(a,b,/,*,c,d):
   print(a + b + c + d)
my_function(5,6,c = 7,d = 8)
   




