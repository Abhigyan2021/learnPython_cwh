
##Dictionaries

# After python 3.7 dictionary is ordered before it was unordered
dic = {
    "Harry": "Human being",
    "Spoon": "Object"
}

print(dic["Harry"])

dic = {
    344: "Harry",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}

print(dic[567])

# #Printing Keys and Values in a dictionary:

info = {'name' : 'Karan', 'age' : 19, 'eligible' : True}

print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The Value Corresponding to the key {key} is {info[key]}")

print(info.items())
for key,value in info.items():
    print(f"The Value corresponding to the key {key} is {value}")



# ## Dictionary Methods

ep1 = {122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566: 90}

ep1.update(ep2)
print(ep1)

ep2.clear()
print(ep2)

empt = {}
print(empt)
 
ep2 = {222:67, 566: 90}
ep2.pop(222) #Removes key value pair of passed key
print(ep2)

ep2 = {222:67, 566: 90, 192: 32, 431: 65}
ep2.popitem()
print(ep2)

#del is used to remove a dictionary item
del ep2[222]
print(ep2)


# for loops with else

for i in range(5):
    print(i)
    if i == 4:
        break # when loop is broken else statement is not print
        #else statement refers to completion of loop and not breaking of loop

else:
    print("Sorry no variable to iterate")

i = 0
while i<7:
    print(i)
    i = i + 1
    if i == 4:
        break

else:
    print("Sorry no i")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of Loop")



