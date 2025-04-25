
#*************method one*********
list=["Mubasir","Danyal","Faham","Safi","Rayyan","Khan"]
Name_5=[]
for x in list:
    if(len(x.upper())>5):
        Name_5.append(x.upper())
print(Name_5)
    
#*********Method2***************

list=["Mubasir","Danyal","Faham","Safi","Rayyan","Khan"]
New_list=[name.upper() for name in list if len(name)>5]
print(New_list)