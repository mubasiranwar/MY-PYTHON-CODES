dict={
    
    "key":"value",
    "Name":"Mubasir",
    "age": 20,
    "marks":[99,89,98,96]   
    
    
}
print(dict)
#acessing a specific key value pair
print(dict["Name"])
print(dict["age"])

#Updating of dictionary/Adding new key value pair

dict["Univercity"]="UET"
print(dict)

#mutiation
dict["age"]=19
print(dict)

#Removing a some key value pair
del dict["age"]
print(dict)
#method 2 for removing a key value pair
dict.pop("Univercity")
print(dict)
