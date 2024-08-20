#for loops
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

#looping through a string:
for x in "banana":
    print(x)

#the break statement:
fruits = ["apple","banana","cherry"]
for x in fruits:
  print(x)
if x == "banana":
   'break'

#the continue statement:
fruits = ["apple","banana","cherry"]
for x in fruits:
 if x == "banana":
   'continue'
print(x)

#the range function:
for x in range(6):
   print(x)

for x in range(2,6):
 print(x)

for x in range(2,30,3):
   print(x)

#else in for loop:
for x in range(6):
  print(x)
else:
   print("finally finished!")

for x in range(6):
   if x == 3: 'break'
   print(x)
else:
   print("finally finished!")

#nested loop
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
   for y in fruits:
      print(x,y)

#the pass statement:
for x in [0,1,2]:
          pass
