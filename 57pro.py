#(61)
list = [1,2,3,4,5,6]
list.remove(4)
print(list)

#(62)
import random
print(random.randrange(1,11))

#(63)
def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]
number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome.")
#else:
    print(f"{number} is not a palindrome.")

#(64)
def find_frequencies(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
frequencies = find_frequencies(my_list)
print(frequencies)

#(65)
def transpose_matrix(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)

#(66)
list1 = [[1], [2,3],[4,5,6,7]]
result = [num for sublist in list1 for num in sublist]
print(result)

#(67)
def sum_of_rows(matrix):
    row_sums = []
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums
matrix = [
       [1,2,3],
       [4,5,6],
       [7,8,9],
]
row_sums = sum_of_rows(matrix)
for i,row_sum in enumerate(row_sums,start = 1):
    print(f"sum of row{i}: {row_sum}")

#(68)
def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    fib = [0, 1]  
    sum_fib = 1  

    for i in range(2, n):
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
        sum_fib += next_fib
    
    return sum_fib
n = 10  
print(f"The sum of the first {n} Fibonacci numbers is: {fibonacci_sum(n)}")

#(69)
def is_perfect_number(n):
    if n <= 1:
        return False
    
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n
number = 28  
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

#(70)
def remove_empty_strings(strings_list):
    return list(filter(None, strings_list))
strings = ["hello", "", "world", "", "python", ""]
result = remove_empty_strings(strings)
print(result)  


