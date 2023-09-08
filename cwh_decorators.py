
#Creation of Decorators in Python

#Decorators take a function and return a function by updating it


#Creating Decorator without Parameter

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thanks for using this function")

#     return mfx

#Creating a Decorator with Parameter

def greet(fx):
    def mfx(*args, ** kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


#Method 1

# @greet 
def hello():
    print("Hello World")

def add(a,b):
    print(a+b)



# or we can use

# greet(hello)()


greet(add)(1,2)