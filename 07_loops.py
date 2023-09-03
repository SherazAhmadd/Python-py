#while loop
x=int(input("enter many time you want to print the sheryy\n"))
print(type(x))
i=0
while (i<x):
    print("sheryy")
    i=i+1
#for loop
for i in range(5,10):
    print(i)
    #end=""  ---> is keyword that print data in same line
print("-----------------")
days = ["m","t","w","t","f","sat","s"]
for d in days:
    # if(d=="sat")break:
    if(d=="sat"): continue
    print(d)