#logical operator
 #and
a = 200
b = 33
c = 500
if a > b and c > a:
    print("both conditions are true")

  #or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("at least one of the conditions is True")

  #not
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

  #nested if
x = 41
if x > 10:
    print("above ten")
    if x > 20:
        print("and also above twenty!")

else:
    print("but not above 50")

  #pass statement
a = 33
b = 200
if b > a:
    pass
   

