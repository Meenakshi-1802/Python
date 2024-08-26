#(41)
n = 5
def print_right_angled_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
print_right_angled_triangle(n)

#(42)
x = int(input("Enter a number: "))
def print_multiples(number,y=10):
   for i in range(1,y + 1):
       print(number * i)
print("The first 10 multiples of",x, "are:")
print_multiples(x)

#(43)
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
       if char in vowels:
            count += 1
    return count


user_string = input("Enter a string: ")
vowel_count = count_vowels(user_string)
print("The number of vowels in the string is:", vowel_count)

#(44)
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
if num2>num1:
    mn = num1
else:
    mn = num2
for i in range(1,mn+1):
    if num1%i==0 and num2%i==0:
        gcd = i
print(f"the GCD of the two numbers is{gcd}")

#(45)
year = int(input("enter a year:"))
if year%4==0:
  print("yes it is a leap year.")
else:
  print("it is not a leap year.")

#(46)
sentence = (input("please enter a sentence:"))
print(sentence.upper())

#(47)
list = {
    "chocolates": 100,
    "biscuits": 50,
    "chips": 50,
    "cake": 200,
    "kurkure":100,
    "icecream":200,

}
price = sum(list.values())
print("the total price of items in a shopping list is",price)

#(48)
birth_year = int(input("enter your birth year:"))
current_year = 2024
age = current_year - birth_year
print("your age is",age,"years")

#(49)
decimal_number = int(input("enter a decimal number:"))
hexadecimal_number = hex(decimal_number)
print("the hexadecimal number is",hexadecimal_number)

#(50)
snumber = int(input("Enter the first number: "))
enumber = int(input("Enter the second number: "))
for number in range(snumber + 1, enumber):
    print("The numbers between", snumber, "and", enumber, "are:")
    print(number)

