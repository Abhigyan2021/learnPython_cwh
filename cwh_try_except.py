
##try-except block


a = ("Enter the number: ")
print(f"Multiplication table of {a} is: ")

try:
  for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
  print(e) # we can print anything error such as print("Invalid Input/ or some other thing")

print("Some imp lines of code")
print("End of Program")


try:
    num = int(input("Enter an integer: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error.")


## finally keyword


# finally keyword always executed but the main difference between it and a normal statement is shown in a function.

#normal code

try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some Error Occurred")
finally:
    print("I am always executed")

print("I am also executed 1")



# code embedded in a function


def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occurred")
        return 0
    finally:
        print("I am always executed")

    print("I am also executed 2") 

x = func1()
print(x)


## Raising Custom Error

a = int(input("Enter any value between 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

# NOTE : we can also create custom error

a = input("Enter any value between 5 and 9: ")


if(a == 'quit'):
    print("Ohk")
elif(int(a) < 5 or int(a) > 9):
    raise ValueError("Value should be between 5 and 9")

 










