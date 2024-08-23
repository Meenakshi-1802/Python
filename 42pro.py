#while loops
#print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

#the break statement
#exit the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#the continue statement
#continue to the next iteration if i is 3:
i = 0
while i < 6:
 i += 1
if i == 3:
   'continue'  #note the number 3 is mising in the result

print(i)

#the else statement
#print a message once the condition is False:
i = 1
while i < 6:
   print(i)
   i += 1
else:
   print("i is no longer less than 6")

