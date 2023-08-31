# print ('Hello World !')
# print ('Hello world , welcome')

# print('Tim is a boy')
# print('Tim is 18 years old')
# print('Tim is from Turkey')

name = 'Tim'

print(name + ' is a boy' )
print(name + ' is 18 years old' )
print(name + ' is from Turkey')

# variable with integer not possible. Hence for concatentation , is a better method than string

age = 21
print(name,'is now',age,'years old') #no need to give space after using ,

# some string functions

print('Tim\'s mother is beautiful')
print('We can print \ just like that but it should not be last character')

# getting particular elements of the string 

sty1 = 'Call Out my name'
print(sty1[0])
print(name[0])
print(sty1[5])
print(sty1[3])
print(sty1[9])
print(sty1[0],sty1[3],sty1[6],sty1[9])

sty2 = 'alllowercase'
sty3 = 'ALLUPPERCASE'
sty4 = 'MiXedCase'

print(sty2.upper())
print(sty3.upper())
print(sty4.upper())
print(sty2.lower())
print(sty3.lower())
print(sty4.lower())

print(sty2.isupper())
print(sty3.isupper())
print(sty4.isupper())

print(sty2.islower())
print(sty3.islower())
print(sty4.islower())

print(sty3.lower().islower())

# finding length and index of string

print(len(sty1))
print(sty1.index('m'))

print(sty1.replace('m', 't'))

# numbers in python

print(78)
print(79 + 22)
print(10*10*3.1415)
print(20/6)
print(20%6)

#converting a number to string

nom1 = 55
nom2 = str(nom1)

print(nom2 + ' is the number')
# print(nom1 + ' is the number') --> gives error

#getting absolute value of a number

print(-5)

# maximum of numbers

print ( max (4, 2))
print( max ( 4, 2, 13, 49, 23, 56))
print(min(4,2))
print(min(4,2,13,16,13,49,23,39))

# rounding off a number

print(round(3.2))
print(round(3.5))
print(round(4.5))

# binary of a number

print(bin(2), bin(3), bin(10))

# to calculate binary number of large numbers we need to use mathematical libraries

from math import *

print(bin(334))
print(sqrt(100))

#Getting user's Input

name = input ('Input your name : ')
age = input ('Input your age : ') # here age is string

print( 'Your name is ' + name + ' your age is ' + age)

# simple word replacement program

liner1 = input('Enter your sentence : ')
print('Your sentence is : ', liner1)
wordo1 = input('Enter a word to replace : ')
wordo2 = input('Enter a word to replace it with : ')
print(liner1.replace(wordo1, wordo2))


