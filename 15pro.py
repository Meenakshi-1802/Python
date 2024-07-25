#Lists in python
marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.1

marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

student = ["karan" , 85 ,"delhi"]
print(student[0])
print(student[1])
print(student[2])

#List slicing
marks =[85,94,76,63,48]
print(marks[1:4])
print(marks[-2:-1])

#Lists Method
list = [2,1,4]
list.append(5)
print(list)

list = [2,1,3]
print(list.sort())
print(list)

list = [2,1,3,4]
print(list.sort(reverse=True))
print(list)

list =['a' , 'b' ,'c' ,'d']
list.reverse()
print(list)

list = [1,2,3,4,5]
list.insert(2,8)
print(list)

list = [2,3,4,5]
list.remove(4)
print(list)

list = [1,2,3,4]
list.pop(1)
print(list)
