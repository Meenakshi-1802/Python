#(31)
x = input("please enter a sentence:")
y = x.split()
for word in y:
    print(y)

#(32)
x = [11,22,33,44,55]
for i in x:
    print(i)

#(33)
numbers = [11+12+13+14+15+16+17+18]
result = sum(numbers)
print(result)

#(34)
my_list = [1,2,3,10,24,6]
print(min(my_list))

#(35)
fruits = ["peach","guava","cherry"]
for fruits in fruits:
  print(fruits)

#(36)
name = input("please enter your name:")
reversed_name = name[::-1]
print(reversed_name)

#(37)
num = int(input("please enter a number:"))
print("Divisors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

#(38)
num = int(input("enter the number of terms:"))
print("fibonacci seuence")
a, b = 0, 1
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b

#(39)
num = int(input("Enter a number:"))
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total
print("Sum of digits:", sum_of_digits(num))

#(40)
binary_num = input("Enter a binary number:")
decimal_num = int(binary_num, 2)
print(decimal_num)

