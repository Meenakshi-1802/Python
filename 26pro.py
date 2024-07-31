#OOP
#del keywprd
class student:
    def __init__(self,name):
        self.name = name

s1 = student("meenakshi")

del s1
print(s1)

#private(like) attributers and methods
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = account("12345" , "abcde")

print(acc1.acc_no)
print(acc1.__acc_pass)

#inheritance
class car:
    @staticmethod
    def star():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped.")

class toyotacar(car):
    def __init__(self,name):
        self.name = name

car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.star())

#super method
class car:
    self.type = type

@staticmethod
def start():
    print("car started..")

@staticmethod
def stop():
    print("car stopped..")

class toyotacar(car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1 = toyotacar("prius" ,"electric")
print(car1.type)

#class method
class person:
    name = "anonymous"
    def changename(self,name):
        self.name = name

p1 = person()
p1.changename("meenakshi palai")
print(p1.name)
print(person.name)

#polymorphism
print(1+2)
print("apna" + "college")
print([1,2,3] + [4,5,6])

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

num1 = complex(1,3)
num1.shownumber()

num2 = complex(4,6)
num2.shownumber()