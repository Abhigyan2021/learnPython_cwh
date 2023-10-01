
#dir() method - It tell us about all the methods associated with a particular data type and their uses

x = [1,2,3]
print(dir(x))
print(x.__add__)

y = (4,5,6)
print(dir(y))
print(y.__init__)

#dict() method = It tell us about all the properties of a class
# and return them in dictionary format

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)

# help() method - It returns all the documentation related to a particular class

#NOTE : If we don't pass any objects or class in help() then we enter the python help environment
print(help(Person))