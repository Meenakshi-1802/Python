#slicing operator
h1 = [6,7,8,1,34,44,56,66,67,51]
p = h1[2:6:2]
print(p)

h1 = [6,7,8,1,34,44,56,66,67,51]
p = h1[5::]
print(p)

#negative indexing
h2 = [91,62,33,14,55,7]
print(h2[-1])

h2 = [91,62,33,14,55,7]
x = h2[-1::-1] #reverse
print(x)

x = "meenakshi"
i = x[0]
print(i)

x = "meenakshi"
i = x[1:5]
print(i)

x = "meenakshi"
i = x[-1::-1]
print(i)
