
#INHERITANCE IN PYTHON

class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


#Programmer class Inherits Employee class

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Karn Tiwari", 4100)
e2.showDetails()
e2.showLanguage()

