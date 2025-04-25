#Create a Set
set={1,2,3,4,5}

#add element in set
set.add(6)
print(set)

#Remove an element from set
set.remove(5)
print(set)

#Checkinng ELement in a list
print(2 in set)
#Uninon Of Sets
set1={1,2,3,4,5}
set2={2,4,6}
print(set1.union(set2))

#Intersection of sets
set3={1,2,3,4,5}
set4={2,4,6}
print(set3.intersection(set4))
      
#Difference In sets

set5={1,2,3}
set6={3,4,5}
print(set5.difference(set6))

#symetric Difference in set
set7={1,2,3}
set8={3,4,5}
print(set7.symmetric_difference(set8))

#checking subset of a set
set9={1,2,3,4,5}
set10={1,2,3,4}
print(set10.issubset(set9))




