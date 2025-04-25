#****Method Ist for finding factorial of list*******
list=[1,0,3,5,6]
New_list=[]
fact=1
for i in list:
    for n in i+1,1:
        fact=fact*n
    New_list.append(fact)
    fact=1
print(New_list)


#****Method 2nd for finding factorial of list*******
import math
list=[1,0,3,5,6]
fact_list=[math.factorial(x) for x in list]
print(fact_list)