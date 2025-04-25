# def sum_number(number):#for use to get any number of integer
#     return sum(number)

# #to accept number of argument given in tuple()
# c=sum_number((int(input("Enter Your a :")),int(input("Enter Your b :")),int(input("Enter Your a :"))))
# print(c)      #*********tUPLE LIKE ARGUMENT IF NO * IS USED IN PARAMETER

def add(*tuple):
    sum=0
    for i in tuple:
        sum=sum+i
    print(sum)

add(1,2,3,4)      #notuple like argument if *parameter is use 

