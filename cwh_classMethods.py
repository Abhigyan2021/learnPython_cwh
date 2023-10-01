
'''
CLASS METHODS

Class Methods are achieved by using @classmethod decorator
'''

#NOTE : We generally pass the parameters as instance but sometimes we may need to pass them as class, here we use CLASSMETHODS decorator
#NOTE : Hence we Use def funcName(cls, OTHER_parameterse) where cls is not a keyword

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    def changeCompany2(cls, newCompany):
        cls.company = newCompany


    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Harry"   
e1.show()
e1.changeCompany2("Tesla")
e1.show()
print(Employee.company)
e1.changeCompany("Google")
e1.show()
print(Employee.company) 