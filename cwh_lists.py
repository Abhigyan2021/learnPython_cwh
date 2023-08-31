
'''
Basics of List
'''

marks = [3,5,6,"Harry",True]

print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print("Negative Indexing")

print(marks[-3]) #Negative index 
print(marks[len(marks)-3]) #Positive index
print(marks[5-3])#Positive index
print(marks[2])#Positive index

'''
Finding an Element in list
'''

if 7 in marks:
    print("Yes")
else:
    print("No")

if "Harry" in marks:
    print("Yes")
else:
    print("No")

if "6" in marks:
    print("Yes")
else:
    print("No")

if "arry" in "Harry":
    print("Yes")
else:
    print("No")

# Note : Same thing applies for strings as well

marks = [3,5,6,"Harry",True,6,7,2,32,345,23]

print(marks)
print(marks[1:-1])
print(marks[1:4:2])

print(marks[1:8])
print(marks[1:8:2])

'''
List Comprehension
''' 

lst = [i*i for i in range(4)]
print("list is",lst)
lst = [i*i for i in range(10) if i%2==0 ]
print("New list is",lst)

'''
List Methods
'''

l = [11,45,1,4,6]

print("list before appending",l)
# l.append(2,7) --> WRONG approach
l.append(2)
l.append(7)
print("list after appending",l)

l.sort()
print("list elements in ascending order:",l)
l.sort(reverse=True)
print("list elements in descending order:",l)


l = [7,2,6,3,1,46,76,34]
print("New List:",l)
l.reverse()
print("After Reversing the list", l)

'''
Finding index of occurrence of an element
'''

l = [11,45,1,2,4,6,1,1]
print("The list is",l)
print("The index of occurrence of element is:", l.index(1))
print("The number of times 1 has occurred in list:", l.count(1))

'''
creating reference of a list
'''

m = l
# m[0] = 0
# print(m) --> m is actually reference of list
print(l)

n = l.copy()
n[0] = 0
print(n)
print(l)

'''
Inserting elements in list
'''

n.insert(1,899) # Inserts 899 at index 1
print(n)

'''
Extending a list
'''

m = [900,1000,1100]
l.extend(m)
print("List after extending",l)

'''
concatenating two lists
'''

k = m + l
print('Concatenation of two list is:',k)


##Tuples 

tup = (1,2,76,342,32, "green", True) #Tuple is immutable
# tup[0] = 30 --> wrong step

print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 342 in tup:
    print("Yes 342 is present in this tuple")

tup2 = tup[1:4] # A new tuple is created
print(tup2)

'''
Tuple Methods
'''

#converting a tuple 

countries = ("spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

#Merging of Tuples

countries = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#Counting Occurrences of elements in a tuple

tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.count(3)
print('count of 3 in tuple1 is:', res)

#Finding Index of an element

res = tuple1.index(3)
print("First Occurrence of 3 is:", res)

#res = tuple1.index(311) --> raises a value error

res = tuple1.index(3,4,8)
print("The value of 3 has index b/w 4 and 8:", res)

res = len(tuple1)
print('length of tuple1 is:',res)




















