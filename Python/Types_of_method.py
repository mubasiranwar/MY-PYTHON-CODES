
#********************TYPES OF METHOD**************
'''
        THER ARE THREE MAIN  TYPES OF METHOD 
    1):- STATIC METHOD:
           
                    it is simple method whic donot need any argument
    Example:-
     # @staticmethod    
    # def show():
    #     print(f"The subject is python")
    DECORATOR:
            @staticmethod

    2):-CLASS METHOD:-
                    The method is used to acess the class atibute it is espically used for if class 
                    claas contain same name claas and object attribte.......... 

     2):-INSTANCE METHOD:-
                    The method is used to acess the OBEJECT atibute ...by defalt also acess class atributr
'''


class student:
    subject="python"
    def __init__(self,name,age):#this is type of instnce method
        self.name=name 
        self.age=age
    # @staticmethod    
    # def show():
    #     print(f"The subject is python")
    # @classmethod
    # def show(clas):
    #     print(f"The subject is {self.subject}")
    
    # @classmethod    #tis is class method the main di
    # def show(cls):
    #     print(f"The subject is {cls.subject}")
        
o1=student("Mubasir",23)
o1.subject="C++"
o1.show()