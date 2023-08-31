## ForLOOP

name = 'Abhigyan'

for i in name:
    print(i)
    if(i == "b"):
        print("This is something special")


'''
Accessing list elements each characters
'''

colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
    for c in color:
        print(c)
    
    print(color)


'''
Printing numbers
'''

for k in range(5):
    print(k+1)

for k in range(1,20001):
    print(k)

for k in range(1, 12, 3):
    print(k)


## WHILE LOOP

#Incrementing While Loop

i = int(input("Enter the number: "))
while(i<=10):
    # i = int(input("Enter the number: "))
    print(i)
    i = i + 1

print("done with the loop")

#Decrementing While Loop

count = 5
while(count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")


## Break and Continue


# break

for i in range(12):
    if(i == 10):
        break;
    print("5 x", i+1, "=", 5*(i+1))

print("out of loop now")


# continue

for i in range(12):
    if(i == 10):
        print("skipped Iteration")
        continue
    print("5 x", i+1, "=", 5*(i+1))


'''
Imitating Do While Loop
'''


i = 0

while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break