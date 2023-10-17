
#Method Overriding
#NOTE : method overrriding is used to change the method definition within a child class which is inherited by parent class

class Shape:
    def __init__(self,x,y):
        self.x = y
        self.y = y
    
    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius
    
rec = Shape(3,5)
print(rec.area())

c = Circle(10)
print(c.area())

  