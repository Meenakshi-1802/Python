#logical operator
temp = int(input("what is the temperature outside ?:"))
if temp >= 0 and temp <= 30:
    print("the temperature is good today !")
    print("go outside!")

elif temp < 0 or temp > 30:
    print("the temp is bad today !")
    print("stay inside !")