list=[1,2,3,1,4,1]
replace=input("Enter The Replace Data :")
list[:]=[replace if i==1 else i for i in list]
print(list)