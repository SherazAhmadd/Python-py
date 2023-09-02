#using conditional operators
# ==,!=,<,>,<=,>=
print("the greater operator:\n",10>9)
print("the lessier operator:\n",10<9)
print("exact equal to:\n",10==9)
print("not equal to:\n",10!=9)
print("less then or euqal to:\n",10<=9)
print("greater then or equal to:\n",10>=9)
print("----------------------------------")

#taking input with condition operator
allow=5
age=(input("enter your age\n"))
print(type(age))
#type conversion from string to int
age = float(age)
print(type(age))
print(age>allow)
