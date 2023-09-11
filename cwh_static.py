
# @staticmethod decorator is present in python which helps in calling method without using instance of the class it is present in


class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b
    

#result = Math.add(1,2)
#print(result) # Output : 3

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7,2))
print(a.add(10,7))