#(21)
name = "meenakshi"
print(name.upper())

#(22)
original_string = "Hello user!Welcome to programming"
substring_to_replace = "user"
replacement_substring = "universe" 
new_string = original_string.replace(substring_to_replace,replacement_substring)
print(new_string)

#(23)
txt = "The best things in life are free!"
print("free"in txt)

#(24)
name = "Hello Universe!"
print(name[0])

#(25)
age = int(input("Enter your age:"))
if age >= 21:
    print("You are an Adult!")
elif age <= 15:
    print("You are a minor")
else:
    print("You haven't been born yet!")

#(26)
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#(27)
num = int(input("enter a number:"))
fact = 1
a = 1
while a <= num:
    fact = fact*a
    a = a+1
    print("the factorial of",num,"is",fact)

#(28)
string = "Burger"
reversed_string = string[::-1]
print(reversed_string)

#(29)
value = input("enter the value to check for palindrome:")
reval =value[::-1]
if value == reval:
    print("yes it is palindrome")
else:
    print("no it is not a palindrome")

#(30)
name = "meenakshi"
print(name.count("e"))

 














