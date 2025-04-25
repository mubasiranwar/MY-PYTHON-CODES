def Cheking_list(list):
    if(len(list)!=len(set(list))):
        print("List contain Duplicate value")
    else:
        print("Not Duplicate")
Cheking_list([1,2,3,4,2])