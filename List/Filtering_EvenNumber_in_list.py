#Obtaing even number from list in inserting into anther list method one
list=[1,2,3,4,5,6,45,768]
liste=[]
for x in list:
    if(x%2==0):
        liste.append(x)
print(liste)

#*********Method 2 comprehension list********

list1=[3,76,57,86,45]
Even_list=[x for x in list1 if x%2==0]
print(Even_list)