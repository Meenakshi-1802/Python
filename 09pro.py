#single line if / Ternary Operator
food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

#clever if / Ternary operator
age = int(input("age : "))
vote = ("yes" , "no") [age >= 18]