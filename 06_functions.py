# defining the function is following
# def is keyword that define the function in python 
def setdata():
    text="sheryy is veryy cool guy"
    print(text)
    print(text)
    print(text)
    print(text)
    # calling the function
setdata()
print("---------------------")
#  function with arguments
def enput(age):
    age= age + 10
    print (float(age))
enput(6)
print("...........................")
# function with the conditional statment
def grades(temp):
    total = 100
    if temp == total:
        print("you get full marks")
    elif temp < total:
        print("you got less marks")
    elif temp > total:
        print("tu top hai putr")

marks = int(input("enter your marks: \n")) 
grades(marks)
