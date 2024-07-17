#conditional statement
#Traffic light code
light = input("light colour : ")
if(light == "red"):
      print("stop") 
elif(light == "yellow"):
      print("look")
elif(light == "green"):
      print("go")
else:
      print("light is broken")

 #grades of students
marks = input("marks : ")
if(marks >= 90):
      print("A")
elif(marks >= 80 and marks < 90):
      print("B")
elif(marks >= 70 and marks < 80):
      print("C")
else:
      print("D")