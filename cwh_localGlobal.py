
#The use of local and global variables


x = 4 #this is global variable
print(x)


def hello():
    x = 5 #this is local variable
    y =1

    print(f"The local x is {x}")
    print("Hello Abhigyan")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")


# print(f"y is {y}") #gives error


## Use of global keyword


x = 10 #global variable

def my_function():
    global x 
    x = 4
    #can't do global x = 4
    y = 5
    print(f"y is {y}")

my_function()
print(f"x is {x}")

