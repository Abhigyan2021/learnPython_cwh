
'''
CLASS METHODS

Class Methods are achieved by using @classmethod decorator
'''

#NOTE : We generally pass the parameters as instance but sometimes we may need to pass them as class, here we use CLASSMETHODS decorator
#NOTE : Hence we Use def funcName(cls, OTHER_parameterse) where cls is a keyword when @classmethod decorator is used.

# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"The name is {self.name} and company is {self.company}")

#     def changeCompany2(cls, newCompany):
#         cls.company = newCompany


#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany


# e1 = Employee()
# e1.name = "Harry"   
# e1.show()
# e1.changeCompany2("Tesla")
# e1.show()
# print(Employee.company)
# e1.changeCompany("Google")
# e1.show()
# print(Employee.company) 

'''
Using Class Methods as Alternative Constructor
'''

##Suppose we have a task at hand to create objects with their information given in string format
## So we can do that by using classmethods as alternative constructors

class Employee2:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

    
e3 = Employee2("Harry", 12000)
print(e3.name)
print(e3.salary)

string = "John-16000"
#e2 = Employee2(string.split("-")[0],int(string.split("-")[1]))
e2 = Employee2.fromStr(string)
print(e2.name)
print(e2.salary) 