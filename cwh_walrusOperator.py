
# Walrus Operator

# Walrus operator is used to assign values to variables within an expression
# ':' is known as walrus operator
# It is added in version 3.8 onwards.

#Example

## Without Walrus operator

a = True
'''
print(a = False) #Error in python
'''

## With Walrus Operator

print(a:=False)


#Example 2

numbers = [1,2,3,4,5]
while(n:= len(numbers)) > 0 :
    print(numbers.pop())


#Example 3

## Without Walrus

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# for food in foods:
#     print(food)


# With Walrus

foods = list()

while(food := input("What food do you like?: ")) != "quit" :
    foods.append(food)

for food in foods:
    print(food)