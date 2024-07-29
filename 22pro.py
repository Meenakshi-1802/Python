#Recursion
def factorial(n):

   #base case
   if n == 0:
       return 1
   #recursive case
   ans = n * factorial(n-1)
   return ans

n = int(input("enter n:"))
print(factorial(n))

#ques-1
def print_n_to_1(n):

    #base case
    if n==0:
        return
    
    print(n)
    #recursive case
    print_n_to_1(n-1)

print_n_to_1(5)

#ques-2
def sum_1_to_n(n):
    #base case
    if n==1:
        return 1
    
    #recursive case
    ans = n +sum_1_to_n(n-1)
    return ans

n = int(input("enter n:"))
        
print(sum_1_to_n(n))

#ques-3
def power_a_b(a,b):
    #base case
    if b==0:
        return 1
    #recursive case
    ans = a + power_a_b(a,b-1)
    return ans

a = int(input("enter a: "))
b = int(input("enter b: "))

#ques-4
def fibonacci(n):
    #base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return(fibonacci(n-1)  + fibonacci(n-2)) #recursive case
    
n = int(input("enter n :"))
print(fibonacci(n))
    