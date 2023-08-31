
## Sets in python

# s = {2,4,2,6}
# print(s)

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# jack = {}
# print(type(jack))
# harry = set()
# print(type(harry))

# for value in info:
#     print(value)


##Set Methods

# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.union(cities2)
print(cities3)
print(type(cities))

cities3 = cities.intersection(cities2)
print(cities3)
cities.intersection_update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}


cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities3 = cities.difference(cities2)
print(cities3)

print(cities.isdisjoint(cities2))

cts1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cts2 = {"Seoul", "Kabul"}
cts3 = {"Seoul", "Madrid", "Kabul"}
print(cts1.issuperset(cts2))
print(cts1.issuperset(cts3))

print(cts1.issuperset(cts3))


cts1.add("Helsinki")
print(cts1)

#remove gives error if element is not present but discard does not show any error in given condition.

cts1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cts1.remove("Tokyo2")
# print(cts1)
#  KeyError: 'Tokyo2'
cts1.discard("Tokyo2")


cts1.add("Helsinki")
print(cts1)
cts1.remove("Helsinki")
print(cts1)
 

item = cts1.pop()
print(cts1)
print(item)

#deleting a set
del cts1
#print(cts1) # --> this will show error because set is already deleted

#Emptying a set
cts1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cts1.clear()
print(cts1)


#Checking if an element is present in list
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is Present.")
else:
    print("Carls is absent.")




