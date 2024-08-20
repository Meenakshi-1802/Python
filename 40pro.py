                               #if statements
a = 33
b = 200
if b > a:
    print("b is greater than a")

                               #elif statements
a = 33
b = 33
if b > a:
    print("b is greater than a")  
elif a == b:
    print("a and b are having same values") 

                               #else statements
a = 200
b = 33
if b > a:  
    print("b is greater than a") 
elif a == b:
    print("a and b both are having same values")    
else:
    print("a is greater than b")   

#we can also have an else without the elif:
a = 200
b = 33
if b > a:
    print("b is greater than a")   
else:
    print("a is greater than b")   

#if we have only one statement to execute,we can put in the same line as the if statement:
if a > b: print("a is greater than b")   

#ternary operaor:[if we have only one statement to execute one for if,one for else]
a = 22
b = 330
print("A") if a > b else print("B")

#we can also have multple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
                             

