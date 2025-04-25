class Animals:
    pass

class Pets(Animals):
    pass

class dog(Pets):
    @staticmethod
    def show():
        print("Bow Bow!")
        
o1=dog()
o1.show()
