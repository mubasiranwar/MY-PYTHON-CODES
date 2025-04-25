paper1=int(input("Enter Paper1 marks :"))
paper2=int(input("Enter Paper2 marks :"))
paper3=int(input("Enter Paper3 marks :"))

prcnt1=(paper1/100)*100
prcnt2=(paper2/100)*100
prcnt3=(paper3/100)*100

totl_prcnt=(prcnt1+prcnt2+prcnt3/300)*100

if(prcnt1>=33 and prcnt2>=33 and prcnt3>33 and totl_prcnt>=40):
    print("Student ae Pass")
else:
    print("Student are Fail")