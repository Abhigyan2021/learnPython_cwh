# Loops in python

# While loops : 
i = 1
while i < 6 or i == 6: 
    print(i)
    i += 1

## Iterating over a string in python

print('\n')

string_to_iterate = "Machine Learning"
char_index = len(string_to_iterate) - 1

while char_index >= 0:
    print(string_to_iterate[char_index])
    char_index -= 1


# For loop : 

print('\n')

## Traversing a string

for  x in 'Hello':
    print(x)

## Traversing a list

lst1 = ['ji', 'ju', 'jo']

print('\n')

for items in lst1 :
    print(items)

## Traversing a dictionary

dict1 = {
    'name' : 'john',
    'age' : 13
}

for values in dict1 :
    print(values)

# break in loop    

print('\n')

for values in lst1:
    print(values)
    if values == 'ju':
        break

## Traversing a range of numbers

print('\n')

for x in range(10) :
    print(x)

print('\n')

for x in range(3,7):
    print(x)    
else : 
    print('finished Looping !')    

# Concept of 2D Lists

lst2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for lists in lst2 : 
    print(lists)

print('\n')

## Printing each element of 2D list individually

for lists in lst2 :
    for row in lists : 
        print(row)

## Note : Comments in python can be used by '#' or " ''' " mark opening and closing

## Building a basic mathematical operations calculator for practice

nom1 = int(input('Enter First Number : '))
nom2 = int(input('Enter Second Number : '))
op1 = input("Enter a Operator : ")

if op1 == '+' :
    print("The Addition of given numbers is : ", nom1 + nom2)
elif op1 == '-' :
    print("The Subtraction of given numbers is : ", nom1 - nom2)
elif op1 == '*' :
    print("The Multiplication of given numbers is : ", nom1 * nom2)
elif op1 == '/' :
    print("The Division of given numbers is : ", abs(nom1 / nom2))
else : 
    print("Invalid Operator")    