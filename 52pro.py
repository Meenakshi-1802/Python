#File Handling
fp = open("a.txt","w")
fp.write("Hello")
print(fp.name)
print(fp.mode)
print(fp.closed)
fp.close()
print(fp.readable())
print(fp.writable())
print(fp)

fp = open("a.txt","w")
n1 = input("enter your name:")
fp.write("ajay")

fp = open("a.txt","w")
l1 = ["india \n","china \n","japan \n","indonesia \n","germany \n"]
fp.writelines(l1)

fp = open("a.txt","r")
print(fp.read(4))
print(fp.readline())
fp = open("a.txt","r")
while True:
    k = fp.readline()
    if k =="":
        break
    print(k,end ="")


