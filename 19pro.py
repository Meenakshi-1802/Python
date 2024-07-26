#Loops in python
count = 1
while count <= 5 :
    print("hello")
    count += 1

print(count)

i = 1
while i <= 5 :
    print("meenakshi")
    i += 1
    print(i)


#Question-1
i = 1
while i <= 100 :
    print(i)
    i +=1

#Question-2
i = 100 
while i >= 1 :
    print(i)
    i -= 1

#Question-3
i = 1
while i <= 10 :
    print(3*i)
    i += 1

#Question-4
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(idx)
    idx += 1

#Question-4
nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i < len(nums) :
    print(nums[i])
    i += 1

#Break & Continue
i = 1
while i <= 5 :
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")

i = 0
while i <= 5 :

    if(i == 3) :
       i += 1 
       continue
    print(i)
    i += 1

list = [1,2,3,4,5]

for val in nums :
    print(val)

tup = (1,2,3,4,5,6)

for num in tup :
    print(num)

nums =[1,4,9,16,25,36,49,64,81,100] 

for el in nums :
    print(el)

nums =(1,4,9,16,25,36,49,64,81,100,49) 
x = 49

for el in nums :
    if(el == x ):
        print("number found at idx" , idx)
    idx += 1

#Range
seq = range(5)
print(range(5))
for i in range(5) :
    print(i)

#pass
for i in range(5) :
    pass

print("some useful work")



