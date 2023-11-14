
#Operator Overloading

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        # we can either return it in vector format or string format
        #String format
        # return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
        #vector format
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)


#There are different __operator__ which may be used to overload different arithmetic operators
#Such as __add__ overloads '+' operator

v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,2,9)
print(v2)

print(v1+v2)
