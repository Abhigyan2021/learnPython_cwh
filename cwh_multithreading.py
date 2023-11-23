
#Multithreading - Used to parallely execute tasks

import threading
import time


def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


# Normal Function Calling

time1 = time.perf_counter()
func(4)
func(2)
func(1)
time2 = time.perf_counter()

time3 = time2 - time1

print(f"Using normal function calling, execution takes {time3} seconds")


# Function Calling using threading

time4 = time.perf_counter()

t1 = threading.Thread(target = func, args=[4])
t2 = threading.Thread(target = func, args=[2])
t3 = threading.Thread(target = func, args=[1])


t1.start()
t2.start()
t3.start()

# time5 = time.perf_counter()
# time6 = time5 - time4
# print(f"Using Threading Function Calling without using join() method we get {time6} seconds")

t1.join()
t2.join()
t3.join()

time7 = time.perf_counter()
time8 = time7 - time4
print(f"Using Threading Function and calling join() method we get {time8} seconds")

