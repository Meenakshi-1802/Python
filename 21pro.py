#Functions Definition 
def calc_sum(a,b): #parameters
    sum = a + b
    print(sum)
    return sum

calc_sum(5,10) #function call ; arguments
#more lines of code
calc_sum(2,10)

calc_sum(12,17)

#average of 3 numbers
def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(1,2,3)

#types
print("meenakshi" ,"python") #sep = " "
print("meenakshipalai",end=" ") 
print("python is a programming language")

#quest-1
cities = ["delhi" , "gurgaon" , "pune" , "noida"]
heros = {"thor" , "ironman" , "spiderman" ,"batman"}
print(heros[0],end=" ")
print(heros[1],end=" ")
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heros)

def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(heros)
print()

#ques-2
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =" , inr_val, "INR")

    converter(73)


