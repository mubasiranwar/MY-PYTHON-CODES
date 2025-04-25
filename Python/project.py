import random
n=random.randint(1,100)
a=-1
guesses=0

while(a!=n):
    
    a=int(input("Guess Number :"))
    if(a>n):
        print("Pleas Enter lower number")
        guesses+=1
    elif(a<n):
     print("Please Enter greater number")    
    guesses+=1
     
     
print(f"The guesses time number  is {guesses} and Number is {a}")
