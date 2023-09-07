
#How to build classes and objects in python

class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

    
a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"


b.name = "Nitika"
b.occupation = "HR"

a.info()
b.info()
c.info()