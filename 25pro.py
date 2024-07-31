#OOP
#class and object :
class student:
    name = "meenakshi palai"

s1 = student()
print(s1.name)

s2 = student()
print(s2.name)

#__init__ function
class student:
    name = "meenakshi palai"
    def __init__(self):
       print(self)
       print("adding new student in database..")

s1 = student()
print(s1)      
       
class student:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in database..")

s1 = student("alia")
print(s1.name)

s2 = student("kiara")
print(s2.name)

#Methods
def welcome(self):
    print("welcome student")

s1 = student("karan",97)
s1.welcome()

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in marks:
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)

s1 = student("tony stark",[99,98,97])
s1.get_avg()

#static methods
class student:
    @staticmethod #decorator
    def college():
        print("ABC college")

#Abstraction
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = car()
car1.start()



