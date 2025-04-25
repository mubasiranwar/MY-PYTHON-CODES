#creating contaning tuple 1 to 10 digit
my_tuple=tuple(range(1,11))
print(my_tuple)


print(3 in my_tuple)#checking membership


#__________Tuple unpacking____________#
tuple=(1,2,3,4,5)
a,b,*c=tuple
print(a,b,c)

#__________Tuple packing____________#
list=[1,2,3,4,5]
my_tuple1=(*list,)
print(my_tuple1)




















