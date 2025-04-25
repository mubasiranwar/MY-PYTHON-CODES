def Checking_list(list1,list2):
    for x in list1:
        if(x in list2):
            print("True")
            break
    else:
        print("Not Present")
Checking_list([1,2,3,4,5],[7,8])