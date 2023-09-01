
##ENUMERATE in Python

marks = [12,56,32,98,12,45, 1, 4]


# without enumerate we have to manually update index in a loop

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Harry, Awesome")
    index += 1


# but with enumerate with we can get index along with a list item

height = [165,155,170, 195, 205, 135, 154, 167]

for index, cm in enumerate(height):
    print(cm)
    if cm > 170 :
        print("Wow, Tall Boy!")
    if index == 3:
        print("Third Index, Fourth Object")


#We can also start enumerate indexing from 1 or 2 or any other choice of our number

for index, cm in enumerate(height, start = 2):
    if index == 3 or index == 4:
        print(f"Index - {index}, Object - {cm}")
    