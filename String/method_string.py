#1):---upper methodd---->retrurn copy of string
string=" mubasir "
string2="anwar"
print(string.upper())
print(string)


#lower()method---->retrurn copy of string
print(string.lower())


# strip()method used for to remove white space leading and at end---->retrurn copy of string
print(string.strip())
#replace() method used for replace a part(substring) of string with another string
name="Mubasir anwar"
print(name.replace("Mubasir",'faham'))


#find()method use to find tje index of substring .it gives the first occurence index of substring
#***********Note****** The difference b/w index and find methdon are that index method arise error if substring n ot found*********

stringf="MY Name is Mubasir Anwar"
print(stringf.find("is"))

#count() method use for to count the occurence of string number



#partiation(method use to divide a sting into three parts while from enterin substring)
#*********Example****------>mubasir ,partion("as") ---->out--->('mub','as','ir')
stringr="Mubasir"
print(stringr.partition("as"))


#*****startwith()method******** use for if True startwith letter return true*********\
    
    
    
#*****endwith()**********
string76="Safi"
print(string76.ljust(5),end=" ")
print("mubasir")






