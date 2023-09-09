
#ACCESS MODIFIERS IN PYTHON


#NOTE: Access modifiers are implemented by using name mangling in python
#NOTE: self.__methodName performs name mangling and we can access it only indirectly
#NOTE: self._methodName doesn't performs name mangling but is rather taken as a convention for protected variables


# class Employee:
#     def __init__(self):
#         # self.name = "Harry" #can be normally accessed
#         self.__name = "Harry"

# a = Employee()
# print(a.name) #normal method of accessing

#BUT can be accessed indirectly as follows:

# print(a._Employee__name)#can be accessed indirectly
# print(a.__dir__())


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self): #Protected Method
        return "CodeWithHarry"
    

class Subject(Student): #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))


#calling by object of Student class
print(obj._name)
print(obj._funName())
#calling by object of Subject class
print(obj1._name)
print(obj1._funName())



