
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"Factorial of {num} is {fact}")
    
factorial(int(input("Enter your Number :")))

