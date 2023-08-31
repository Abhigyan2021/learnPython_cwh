# Exception Handling 

try : 
    x1 = int(input("Enter a number : "))
    print(x1)
except :
    print("Something went wrong")    
else : 
    print("Nothing went wrong")    

try : 
    x2 = float(input("Enter a floating point Integer : "))    
    print(x2)
except ValueError:
    print("Input Not a Floating Point Integer")    

    ## other errors like NameError Exist

# Reading/Writing a file

# Note : Everytime we open a file we have to close a file 
## Note : we can't readlines() two times in a row

cnlist_file = open('E:/Django Development/Python Learning/cntr1.txt')
print("Is countries list file readable : ",cnlist_file.readable())
print("Printing the first two elements of file ", cnlist_file.readline(), cnlist_file.readline())
# print("Printing everything in file : ")
# print(cnlist_file.readlines())

print("Using loop to access the file elements ")

for lines in cnlist_file.readlines():
    print(lines)

cnlist_file.close()

# write function of python is used to create a new file generally

cnlist_file = open("E:/Django Development/Python Learning/cntr2.txt", "w")
cnlist_file.write('This is the new text')
cnlist_file.write("This is the second text")

# to write on a new line in file we simply use '\n'
cnlist_file.write('\nThis is the third text but on a new line')

cnlist_file.close();

# python program can be used to open a new python file

cnlist_file = open("E:/Django Development/Python Learning/fileTest.py", "w")

cnlist_file.write('print(\'This is a new file in python.\')')

cnlist_file.close();

# Classes and Objects

print("Classes and Objects sections starting here\n")

class MyClass :
    x = 5

p1 = MyClass()    
print(p1.x)

class Person1 :
    def __init__(self,name, age) :
        self.name = name
        self.age = age

p2 = Person1('John', 32)
print(p2.name)
print(p2.age)

name1 = input('Enter your name:')
age1 = input('Enter your age :')

p3 = Person1(name1,age1)
print(p3.name)
print(p3.age)

del p3

# or we can use del p3.name & p3.age

#pass keyword --> Used for Bypassing any error
class Person2 :
    pass

#Inheritance in Python

from fileTest2 import Student1

class Person3(Student1) :
    pass

p4 = Person3() 
print(p4.name, p4.work, p4.alive)
