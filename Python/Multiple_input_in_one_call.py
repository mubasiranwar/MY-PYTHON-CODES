def func(a,b,c):
    if(a>b and a>c):
        return "a is greatrest"
    elif(b>c and b>a):
        return "b is greatrest"
    else:
        return "c is greatrest"
# ************multiple input in one call one funcrion
print(func(int(input("Enter a :")),int(input("Enter b :")),int(input("Enter c :"))))
