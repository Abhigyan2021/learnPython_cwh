
# lists in python

## creating a list
countries1 = ['United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand']

## Accessing a list
print(countries1[0])
print(countries1[1])
print(countries1[2])
print(countries1[3])
print(countries1[-1])
print(countries1[-2])
print(countries1[-3])
print(countries1[-4])
print(countries1[2][0])
print(countries1[1:3])

## list type

print(type(countries1))

## updating values of list elements

countries1[0] = 'United States'
countries1[1] = 'Canada'

print(countries1)

## length of the list

print('length of the arrays is : ', len(countries1))

#  a list may contain multiple different types of variables 

example_list1 = ['United Kingdom', 2, True, 5.9, 'New Zealand']

print(type(example_list1[0]))
print(type(example_list1[1]))
print(type(example_list1[2]))
print(type(example_list1[3]))
print(type(example_list1[4]))

## using list constructor to initialize list

countries2 = list(('United Kingdom', 'Ghana', 'Nigeria', 'Australia', 'New Zealand'))

print(type(countries1))
print(type(countries2))

example_list2 = [1,2,3,4,5]
example_list3 = ['banana', 'apple', 'mango', 'oranges']

## merging two lists

example_list2.extend(example_list3)
print(example_list2)

## adding elements at last of the list

example_list2.append('guava')
print(example_list2)

## inserting an element at the wanted position of the list

example_list2.insert(1, 'cherry')
print(example_list2)

## removing an element from the list
example_list2.remove('cherry')
print(example_list2)

## making a list empty

example_list2.clear()
print(example_list2)

## finding an element in the list

print(example_list3.index('mango'))
# print(example_list3.index('guava')) --> gives error

## counting particular elements occurrence in a list

example_list4  = [48, 34, 56, 48, 34, 56, 67, 23 , 64]

print(example_list4.count(48))

## sorting a list

example_list4.sort()
print(example_list4)

## reversing a list

example_list4.reverse()
print(example_list4)

## copying a list into another list

example_list4 = example_list1.copy()
print(example_list1)

## removing last element from the list

example_list3.pop()
print(example_list3)

example_list3.append('oranges')
# we can also do example_list3.remove('banana')
# or we can write
# del example_list3[0]
example_list3.pop(1)
print(example_list3)

## deleting a list --> different from clear function

del example_list4
## print(example_list4) --> gives error

# Tuples in Python

## Notes : 1) Immutable(elements once defined cannot be changed)
#          2) Each elements can be accessed individually
#          3) Repetition of Values is allowed
#          4) Length can be obtained
#          5) Type function can be used
#          6) Multiple data types can be used in tuple
#          7) Tuple constructor(like list) can be used to create tuples

theeree_nums = (1,2,3)
print(theeree_nums)

str1 = ('home', 'land', 'earth')
print(str1)

mltis = tuple((1, 'name', True, 2 , 3 ,1))
print(mltis)
print(len(theeree_nums), len(str1), len(mltis))
print(mltis[2])
print(type(mltis))

# invalid statement
## mltis[2] = false

# Dictionaries in Python

my_dict = {
    'name' : 'Tim',
    'nationality' : 'African',
    'age' : 87,
    'is_tall' : True,
    'Qualification' : 'College',
    'Friends' : ['Peter', 'Paul', 'Precious']
} 

print(my_dict)
print(my_dict['Friends'])
print(len(my_dict))
print(type(my_dict))

