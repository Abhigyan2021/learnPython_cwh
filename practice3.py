# Functions in python

def greetings_function1():
    print('Welcome User !')

def greetings_function2(name):
    print('Welcome ' + name)

def greetings_function3(name, age):
    print('Welcome ' + name + '. You are ' + str(age) + ' years old.')  

greetings_function1()
greetings_function2('john wick')
greetings_function3('john wick', 42)   

nm1 = input('Enter your name : ')
aj1 = input('Enter your age : ')
greetings_function3(nm1, aj1)


# Return Statement

# n1> usually used at the end of function as after executing return rest statements of function does not execute.

def add_function1():
    return 5 + 4

print(add_function1())

def add_function2(num1, num2):
    return num1 + num2

print(add_function2(23, 37))

## note : since input uses string to take input if we put input taken from user directly in 'add_function2' it will only concatenate them as string.

num3 = input('Enter first number : ')
num4 = input('Enter second number : ')

print(add_function2(num3, num4))

# hence we first convert the input into the integer

num3 = int(num3)
num4 = int(num4)

print(add_function2(num3, num4))

# IF Statements

num5 = 69
num6 = 171

if num5 > 60 : 
    print(str(num5) + ' is greater than 60')

if num6 < 180 : 
    print(str(num6) + ' is less than 180')

if num5 >= num6 : 
    print(num5, 'is greater than or equal to', num6)
elif num5 <= num6 :
    print(num5, 'is less than or equal to', num6)

if not (num5 == num6) : 
    print(num5, 'is equal to', num6)

if num5 != num6 : 
    print(num5, 'is not equal to', num6)

## multiple condition checking in IF statement

gender1 = input('Enter Boy or Girl : ')
height1  = input('Enter short or long basis of 1.65m : ')

if gender1 == 'Boy' and height1 == 'short' :
    print('He is a short boy')
elif gender1 == 'Boy' and height1 == 'long' :
    print('He is a long boy')
elif gender1 == 'Boy' or gender1 == 'Girl' :
    print('He may be a boy or a girl')
else :
    print('She is a girl')


value1 = int(input("Input a value : "))

if type(value1) == str : 
    print(value1 + ' is a string')
else :
   print(value1, 'is not a string')    


