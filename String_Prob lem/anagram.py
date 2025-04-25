'''
ANAGRAM:
        Anagram is a word or phrase formed the letter of another word
        typically using all the orignal letters once exactly once.
        in other word an angram is a recoreded version of string of character 
        Example "acts" and cats
        teams and "meats"

'''
string1=input("Enter string1 ")
string2=input("Enter string2 ")
#removing any white space and conveting into lowercase
string1=string1.replace(" ","").lower() 
string2=string2.replace(" ","").lower()
#doing  sorting and checking sorting 
if(sorted(string1)==sorted(string2)):
    print("Yes Anagram")
else:
    print(print("Not Anagram"))

