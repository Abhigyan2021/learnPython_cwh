
## map function 
# It is used to convert perform on every item of a list through a function

#NOTE: map, filter and reduce are higher order functions
# Higher Order Functions are those functions which can take other functions as arguments


def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,4,6,4,3]


#below function stores cube of every element present in list 'l' to a newlist 'newl'

# newl = []
# for item in l:
#     newl.append(cube(item))


#this work can easily be done by map function

#NOTE: map function returns a map hence it should be converted to list


newl = list(map(cube,l))

print(newl)


## FILTER FUNCTION
#It filters out elements of a list based upon a function


def filter_function(a):
    return a > 4

newnewl = list(filter(filter_function, l))
print(newnewl)

newnewl = list(filter(lambda a: a>=2, l))
print(newnewl)


##REDUCE FUNCTION
#It performs an operation defined in a function upon every element in list and outputs final value

#NOTE: reduce function must be imported


numbers = [1,2,3,4,5]

from functools import reduce

def mySum(x,y):
    return x + y

sum = reduce(mySum, numbers)

#Print the sum
print(sum)
