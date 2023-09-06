a = 4
b = "4"

print(a is b) #checks exact location of object in memory
print(a == b) #checks value

# output : False and False

a = [1,2,43]
b = [1,2,43]

print(a is b) #False because two separate list
print(a == b) #True because value is equal

a = 3 
b = 3

print(a is b) #True because constants are immutable hence created only once in memory in python
print(a == b) # True because value is same

import copy

c = copy.deepcopy(b)

print (a is c)
print("Id of A", id(a))
print("Id of B", id(b))
print("ID of C", id(c))

# same location returned for tuples and keyword "none"
