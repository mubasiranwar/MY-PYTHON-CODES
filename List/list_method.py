#*****append()method*******

list1=[1,2,3]
list1.append(4)
print(list1)

#******extend()method********

list2=[1,2,3,4]
list2.extend([5,3])
print(list2)

#******inserat()method********

list3=[1,3,5,7]
list3.insert(1,2)
print(list3)

#******remove()method********

list4=[1,2,3,4,2,5]
list4.remove(2)#remove first ccurence element in list
print(list4)

#******pop()method********

list5=["cat","dog","khan"]
print(list5.pop(1))#it return the specified removed inderx value


#******clear()method********

list6=[1,2,3,4]
list6.clear()
print(list6)

#******index()method********

list7=[1,2,3,4,5,3]
print(list7.index(3))#return the first ocurence of index of 3 which it occure


#******count()method********
list8=[1,2,3,4,5,3,3]
print(list8.count(3))


#*****reverse()method********
list9=[1,2,3,4]
list9.reverse()
print(list9)

