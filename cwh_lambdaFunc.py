
# Lambda Functions are anonymous functions used to create short functions

#Ex: Below is a simple functions

def double(x):
    return x*2

# which can also be written in form of lambda functions as follows

double = lambda x: x*2

#Functions can be passed as parameters in other functions in python

def appl(fx, value):
    return 6 + fx(value)

#Let us make some more lambda functions

cube = lambda x : x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,5,10))
print(appl(lambda x : x*x, 2))
