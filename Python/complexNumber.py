class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def ShowNumber(self):
        print(f"{self.real} + {self.img}i")
        
    def __add__(self,num2):
        Realp=self.real+num2.real
        Imgnry=self.img+num2.img
        return complex(Realp,Imgnry)
    
num1=complex(2,5)


num1.ShowNumber()
num=complex(3,7) 
num.ShowNumber()
num3=num1+num
num3.ShowNumber()

        
        
        