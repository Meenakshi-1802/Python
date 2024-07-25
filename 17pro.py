#Dictionary in python
info = {
    "key" : "value",
    "name" : "apnacollege",
    "learning" : "coding",
    "age" : 21,
    "is_adult" : True,
}

print(info)

#Nested dictionaries
student = {
    "name" : "meenakshi",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95,

    }
}
print(student["subjects"])
print(student.keys())
print(len(list(student.keys())))
print(student.values())
print(student.items())
print(student.get("key"))
student.update({"city" : "delhi"})

print(student)
