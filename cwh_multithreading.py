
#Multithreading - Used to parallely execute tasks

import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

# Normal Function Calling

# time1 = time.perf_counter()
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()

# time3 = time2 - time1

# print(f"Using normal function calling, execution takes {time3} seconds")


# Function Calling using threading

# time4 = time.perf_counter()

t1 = threading.Thread(target = func, args=[4])
t2 = threading.Thread(target = func, args=[2])
t3 = threading.Thread(target = func, args=[1])


# t1.start()
# t2.start()
# t3.start()

# time5 = time.perf_counter()
# time6 = time5 - time4
# print(f"Using Threading Function Calling without using join() method we get {time6} seconds")

# t1.join()
# t2.join()
# t3.join()

# time7 = time.perf_counter()
# time8 = time7 - time4
# print(f"Using Threading Function and calling join() method we get {time8} seconds")


#Example 2

def poolingDemo():
    with ThreadPoolExecutor() as executor:

        #Method - 1

        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 5)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        #Method - 2

        l = [3,5,1,2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()