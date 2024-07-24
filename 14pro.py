#Conditional statements
age = 21
if(age >= 18):
    print("can vote and apply for licence")
    print("can drive")
    print("can vote")

light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

print("end of code")

marks = 74

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade ="B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->" , grade)

#nesting
age = 34

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")