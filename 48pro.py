#set
a = {1,2,3,4,5,6}
print(a)

s1 = {11,22,33,44,55,66,77,11,33,22,55}
print(s1) #dulicate values can't be store
s2 = {35,48,56,88,79}
s3 = s1.update(s2)
print(s1)

#union
s1 = {1,2,3,4,5,6}
s2 = {4,5,6}
s3 = s1.union(s2)
print(s3)
s4 = s1.intersection(s2)#intersection
print(s4)


