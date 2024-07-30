#File I/O
f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#Reading a file
f = open("demo.txt","r")
data = f.read(5) #reads entire file
print(data)
f.close()

f = open("demo.txt","r")
line1 = f.readline() #reads one line at a time
print(line1)
f.close()

#writing to a file
f = open("demo.txt","a")

f.write("i want to learn javascript tomorrow.123")

f.close()

#with syntax
with open("demo.txt" ,"r") as f:
    data  = f.read()
    print(data)

with open("demo.txt" , "w") as f:
    f.write("new data")

#Deleting a file
import os

os.remove("sample.txt")



