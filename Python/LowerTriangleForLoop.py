# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(i, end=" ")
#     print('')
    
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print('*', end=" ")
#     print('') 
n=int(input("Enter Number Of Rows :"))
for i in range(1,n):
    for j in range(n,i-1,-1):
        print('*', end=" ")
    print('')     