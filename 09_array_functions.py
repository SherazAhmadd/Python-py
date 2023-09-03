import numpy as np
a=np.array([2,3,45.56,8,9.2,54])
print(type(a))
a.sort()
print(a)
print("--------------------------")
b=np.arange(0,10,3)
print(b)
print(b.ndim) #-----> showing dimention
# concetinate both arrays
sum=np.concatenate((a,b))
sum.sort()
print("the sum of both arrays is: ","\n",sum)
print("---------------------------")
# 2-D arrays concetination
x=np.array([[5,4,3,2],[2,3,4,5]])
print("the x array is: ","\n",x)
y=np.array([[0,9,8,7,],[7,8,9,0]])
print("the y array is: ","\n",y)
print("-------------------------")
c=np.concatenate((x,y),axis=0)
print(c)
print("-------------------------")
c=np.concatenate((x,y),axis=1)
print(c)
print(c.ndim) #-----> showing dimention
print("--------------------------")
# converting 1-D to 2-D
d1 = np.array([2, 3, 5, 6, 77, 8, 99, 9, 4])
d2 = d1[np.newaxis,:]
print(d2)
print(d2.ndim)
