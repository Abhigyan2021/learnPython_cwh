name = "Abhi"
friend = "Prathmesh"
anotherFriend = 'Tia'

eatApple = '''He said, Hi Abhi!! hey I am good "I want to eat an apple"'''

print("Hello,", name)

print(eatApple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print("\n")

for character in friend:
    print(character)



##String Slicing



fruit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4]) # including 0 but excluding 4
print(fruit[1:4]) # including 1 but excluding 4
print(fruit[:5]) #It will be considered as [0:5]
print(fruit[0:-3])
print(fruit[:len(fruit)-3]) #equivalent to above
#print(fruit[-1:len(fruit) - 3]) --> wrong statement
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# #Quick Quiz
nm = "Harry"
print(nm[-4:-2])



## String Methods


#Strings are immutable in python --> we can't change them in place

a = "!!!Harry!! !!!!!!!!! Harry!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "john"))
print(a.split("Harry"))

blogheading = "introduction tO jS"
print(blogheading.capitalize())


str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

# #variable overriding possible in python

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))

# #note : find() and index() both work same but on not finding the character find() returns -1 but index() returns error.

str1 = 'WelcomeToTheConsole'
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print("Is this string in lower case", str1.islower())

str1 = "We wish you a Merry Christmas\n"
print("Is this string printable", str1.isprintable()) # because \n is not a printable character

str1 = '            ' #using spacebar
print("Does this string contain space", str1.isspace())
str2 = "                " #using tabs
print("Does this string contain space", str2.isspace())
str3 = "filled    with    spece"
print("Does this string contain space", str3.isspace())

str1 = "World Health Organization"
print("Is thsi string title format",str1.istitle())

str2 = "To kill a Micking bird"
print("Is thsi string title format",str2.istitle())

str1 = "Python is an Interpreted Language"
print("Does this string starts with python:",str1.startswith("Python"))

print("Swapping the cases of string characters:",str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print("converting the string to its title form:",str1.title())



##If Else statements - Conditionals in Python


a =  int(input("Enter your age: "))
print("your age is", a)

#conditional operators
#>,<, >=, <=, ==, !=

print(a > 18)
print(a <= 18)
print(a == 18)
print(a != 18)

#Ex - 1

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
    print("No")
    print("Yay!")

#Ex -2

applePrice = 180
budget = 200

if(budget - applePrice > 50):
    print("Alexa, add 1 Kg Apples to the cart")
elif(budget - applePrice > 10):
    print("Its okay you can buy")
else:
    print("Alexa, do not add Apples to the cart.")

#Ex - 3

num = int(input("Enter the value of num: "))

if(num < 0):
    print("Number is Negative.")
elif(num == 0):
    print("Number is Zero.")
elif(num == 999):
    print("Number is special.")
else:
    print("Number is Positive.")

print("I am happy now.") 


#Ex - 4

num = 18

if(num < 0):
    print("Number is negative.")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1 -10")
    elif(num > 10 and  num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero.")


##Exercise 2 - Good Morning Sir


#Handling Time Module

import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
print(type(timestamp))
timestamp = int(time.strftime('%S'))
print(timestamp)
print(type(timestamp))

import time

hour = int(time.strftime('%H'))

if(hour >= 5 and hour < 12):
   print("Good Morning!")
elif(hour >= 12 and hour <18):
   print("Good Afternoon")
elif(hour >= 18 and hour < 23):
   print("Good Evening")


##Match case statements - only for version above 3.10

#checking python version
# import os 

# os.system("python --version")

#it will not run now

x = int(input("Enter the value of x: "))
#x is the variable to match
# match x:
#     case 0:
#         print("X is Zero")
#     case 4:
#         print("Case is 4")

#     case _ if x != 90:
#         print(x,"is not 90")
#     case _ if x != 80:
#         print(x, "is not 80")
#     case _:
#         print(x)

