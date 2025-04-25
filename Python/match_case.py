def number(n):


    match(n):
        case(1):
            return "A"
        case(2):
            return "B"
        case(3):
            return "C"
        case(4):
            return "D"
        case _:
            return "Wrong number"
print(number(n=int(input("Enter the number :"))))       