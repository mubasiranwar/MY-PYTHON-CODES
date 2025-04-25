#*******************for one number can apply one opration********************
# class calculator:
#    def __init__(self):
#       pass
#    def square(self,num):
#        print(f"square of {num} is {num*num}")
#    def cube(self,num):
#       print(f"Cube of {num} is {num*num*num}")
#    def square_root(self,num):
#        print(f"Square root of {num} is {num**(1/2)}")
      
# r1=calculator()
# r1.square(int(input("Enter number for square :")))
# r1.cube(int(input("Enter number for cube :")))
# r1.square_root(int(input("Enter number for square root :")))

# *********************for one number all opration************************
class calculator:
   def __init__(self,num):
      self.num=num
   def square(self):
       print(f"square of {self.num} is {self.num*self.num}")
   def cube(self):
      print(f"Cube of  {self.num}  is {self.num*self.num*self.num}")
   def square_root(self):
       print(f"Square root of {self.num}  is {self.num**(1/2)}")
      
c1=calculator(int(input("Enter The Number :")))
c1.square()
c1.cube()
c1.square_root()
