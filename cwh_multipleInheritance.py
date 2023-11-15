
## Multiple Inheritance - A single class inherits multiple class

class Employee :
    def __init__ (self,name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")
    
class Dancer:
    def __init__(self,dance):
        self.dance = dance
    
    def show(self):
        print(f"The name is {self.dance}")
    
class DancerEmployee(Dancer,Employee): #here if we change order of dancer and employee arguments then the show methods will be affected.
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
    
o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
#Important Point
o.show()
#Study MRO resolution order in python
print(DancerEmployee.mro())