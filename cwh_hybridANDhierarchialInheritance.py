
#Hybrid Inheritance - Combination of two form of Inheritance

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass


#Hierarchial Inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed : {self.breed}")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Cat")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"Breed : {self.breed}")

class Hamster(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Hamster")
        self.breed = breed
        
    def show(self):
        Animal.show(self)
        print(f"Breed : {self.breed}")

d = Dog("John", "Alsacian")
c = Cat("Phily", "Paris Cat")
h = Hamster("Rob", "SouthWest Hamster")

d.show()
print("\n")
c.show()
print("\n")
h.show()
