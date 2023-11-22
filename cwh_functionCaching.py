
#Function Caching - Performs memoization in python for already executed values of function

#NOTE : Values are stored in cache for only a single run. During every re-run of program it is executed again.


#Example

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*5


print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(61))
print("done for 61")