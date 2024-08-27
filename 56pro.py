#(51)
x = int(input("enter a number:"))
for i in range(2,x):
    if x%i==0:
        print("not prime")
        break
    else:
        print("prime")

#(52)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")

#(53)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
def lcm(a, b):
    while b != 0:
       a, b = b, a % b
    return a
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")

#(54)
list = [3,6,1,8,5,9,0,2]
list.sort()
print(list)

#(55)
my_list = [1, 2, 3, 4, 2, 5, 3, 6, 1]
def remove_duplicates(lst):
    return list(set(lst))
unique_list  = remove_duplicates(my_list)
print("List after removing duplicates:",unique_list)

#(56)
n = 10
natural_numbers = sum(range(1,n+1))
print("the sum of the first",n,"natural numbers is:",natural_numbers)

#(56)
list = [1,12,3,4,5,67,55,33]
largest_num = max(list)
print(largest_num)

#(57)
list = [1,12,3,4,5,67,55,33]
smallest_num = min(list)
print(smallest_num)

#(58)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list", merged_list)

#(59)
squares = [x**2 for x in range(1,11)]
print(squares)

#(60)
def is_sorted(lst):
    return lst == sorted(lst)
my_list = [1, 2, 3, 4, 5]
print(is_sorted(my_list))

#(61)
n = int(input("enter the total number of element we want in our list:"))
l = []
for i in range(n):
    ele = int(input("enter the element:"))
    l.append(ele)
print("my list",l)
sorted_list = l.sort()
print("sorted list",l)
second_largest = l[-2]
print("second largest element",second_largest)

