
## map function 
# It is used to convert perform on every item of a list through a function


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

