# creating array with numpy library
import numpy as np 
a = np.array([3, 4, 5, 6, 1])
print("the array is:", a)
print("Length of the array:", len(a))
print("First element of the array:", a[0])
print("Slicing the array:", a[0:4])
print("Type of the array:", type(a))
print("----------------------------")
# creating 2-D array
b = np.array([[2, 3, 53], [23,4,54], [3, 5, 7]])
print("Type of the 2-D array:", type(b))
print("Number of rows in the 2-D array:", len(b))
print("the 2-D array is:","\n", b)
# creating zero 1-D array
c = np.zeros(3)
print(c)
# creating the one array
d=np.ones(3)
print("the one's array is: ",(d))
# creating range array
e = np.arange(10)
print(e)
# creating range array W specific
f = np.arange(4,10)
print(f)
# creating range array W after interval
t=np.arange(0,10,3)
print(t)
# creating 2-D array's
h=np.arange(9).reshape(3,3)
print("the 2-D array is: ","\n",(h))


