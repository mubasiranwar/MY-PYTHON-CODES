# set={12,3,4,5}
# set2={3,4,5,6}
# diff=set-set2
# print(diff)


# set1={1,2,3}
# set2={3,4,5}
# union=set1|set2
# print(union)


# set1={1,2,3,5}
# set2={3,4,5}
# intersction=set1 & set2
# print(intersction)

my_set={1,2,3}
power_set=[set() for i in range(len(my_set))]
for i,elem in enumerate(my_set):
    for j in range(2**i,2**(i+1)):
        power_set[i].add(elem)
print(power_set)
