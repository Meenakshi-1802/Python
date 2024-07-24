#Strings
str1 = "This is a string."
str2 = 'meenakshi'
str3 = """This is a string"""

"This is apnacollege's tutorial"
'This is apnacollege"s tutorial'

#Escape sequence characters
str1 = "This is a string.we are creating it in python."
print(str1)
str2 = "This is a string.\n we are creating it in python"
print(str2)

#concatenation
str1 = "my name is"
str2 = "meenakshi palai"
finalstr = (str1+str2) 
print(finalstr)

#length
str1 = "apna"
len1 = len(str1)
print(len1)

str2 = "college"
len2 = len(str2)
print(len2)

finalstr = str1 + " " + str2
print(finalstr)
print(len(finalstr))

#Indexing
str = "apna college"
ch = str[1]
print(ch)

#Slicing
str = "apna college"
print(str[1:4])
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

#Negative index
str = "apple"
print(str[-5:-1])

#Functions
str = "I am studying python"
print(str.endswith("hon"))

str = "apna college"
print(str.capitalize())

str = "i am studying python"
print(str.replace("y" , "k"))

str = "i am studying python"
print(str.find("a"))

str = "i am studying python"
print(str.count("y"))



