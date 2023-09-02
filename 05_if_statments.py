school_required = 5
age = int(input("what is  your age: "))
# print(type(age))
if age >= school_required: 
    print('you can study in school')
elif age < school_required:
    print('you are too young to go school')
elif age == school_required:
    print('this is right time to go school')
else:
    print("none")

    

    #elif ---> is else-if statments in python
    # if you want more than one condition, use elif statment