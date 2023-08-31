
#user defined functions

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater or equal")

def isLesser(a,b):
    pass     # this statement leaves the execution of this part

a = 9
b = 8

isGreater(a,b)
calculateGmean(a,b)

c = 8
d = 7

isGreater(c,d)
calculateGmean(c, d)

#Functional Arguments

def average(a,b, c =1):
    print("The average is", (a+b+c)/3)

#Note : In above function a and b are compulsory arguments that need to be passed but c is a default argument as it will take 1 as default value if parameter is not passed.

average(4,6)
average(4, b = 2, c = 3)

#Passing Tuples as an argument

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))

average(1,2,3,4,5,6,7,8,9,10)

#Passing Dictionary as an argument

def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

#what a function returns

c = average(5,6,7,1)
print(c)
