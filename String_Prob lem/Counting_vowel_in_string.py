# string=input("My string is ")
# vowel=0
# for i in string:
#     if i=='a' or 'A' or 'i' or 'I' or 'o' or 'O'or 'u' or 'U' or 'v' or 'V':
#         vowel+=1
#     else:
#         pass
# print(f"The number of vowel in string is {vowel}")

string=input("My string is ")
vowel='aiouvAIOUV '
count=0
for i in string:
    if i in vowel:
        count+=1
print(count)
        