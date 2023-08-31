
'''
fstrings for string formatting
'''

#Note : fstrings are introduced in version 3.6

letter = "Hey my name is {1} and I am from {0}" #--> we may or may not use numbers here
country = "India"
name = "Eddie"

#without fstrings
print(letter.format(country,name))

#with fstrings
print(f"Hey my name is {name} and I am from {country}")

#without fstrings
txt = "For only {price: .2f} dollars!"
print(txt.format(price = 49.09999))

#with fstrings
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(type(f"{2*30}"))

print(f"Hey my name is {{name}} and I am from {{country}}")

'''
Docstrings and PEP-8 
'''

def square(n):
    '''
    Takes in a number n, returns the square of n
    '''

    # Above is a docstring and docstring must be written just below function name and just above function definition.

    print(n**2)

square(5)
print(square.__doc__)

#Pep - 8 is a guideline for making good structured programs

#Recursion

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))
    

def fib(n):
    if(n == 0 or n == 1):
        # print(n)
        return n
    else:
        x = fib(n-1) + fib(n-2)
        # print(x)
        return x

print(fib(5))

for i in range(9):
    print(fib(i), end = " ")






