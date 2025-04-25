TwoD_list=[[1,2,3],[4,5,6],[7,8,9]]
print(TwoD_list[1][1])#acessing of element
print(TwoD_list)

#********for finding dignal of 2D matrix
Dignal_2D_matrix=[TwoD_list[i][i] for i in range(len(TwoD_list))]



for i in TwoD_list:
    print(i)#itreting over row
    
    
    
for j in zip(*TwoD_list):#******Iterating over column
    print(j)



ThreeD_list=[[[1,2,3],[5,6,7],[6,3,6]],[[1,2,3],[4,5,6],[7,8,9]]]
print(ThreeD_list)