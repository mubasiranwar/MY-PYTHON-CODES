numbers=[1,2,3,4]
letters=['a','b','c']
combination_1=[(x,y) for x in numbers for y in letters]
print(combination_1)


numbers=[1,2,3,4]
letters=['a','b','c']
combination_2=[(x,y) for x in letters for y in numbers]
print(combination_2)