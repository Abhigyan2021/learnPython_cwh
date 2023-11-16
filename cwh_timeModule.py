
#Time Module in Python

import time


## time() method

def usingWhile():
    i = 0
    while(i < 5000):
        i = i + 1
        print(i)

def usingFor():
    for i in range(5000):
        print(i)

init = time.time()
usingWhile()
t1 = time.time() - init

init = time.time()
usingFor()
t2 = time.time() - init

print(f"Time for Running While Loop is : {t1}")
print(f"Time for Running For LOOP is : {t2}")


## sleep() method

print("\n")
print(4)
time.sleep(20)
print("This is printed after waiting 20 seconds")

## localtime() method

t = time.localtime()

## strftime() method

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)

