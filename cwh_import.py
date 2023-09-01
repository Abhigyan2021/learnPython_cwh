
## Working of import function

#importing complete module 


# import math

# res1 = math.floor(4.2343)
# print(res1)


#importing selected functions from a module


# from math import sqrt,pi

# res2 = sqrt(9)*pi
# print(res2) #output: 3.0*pi


#importing all functions from a module


# from math import *

# res3 = floor(4.677) + sqrt(9)*pi
# print(res3)


# 'as' method


#from math import * as s --> wrong
#from math import pi, sqrt as s --> import sqrt functions as s from math module

import math as m

res4 = m.sqrt(9)*(m.pi)
print(res4)


#printing all directories of maths


print("list of directories of math module",dir(m))


#getting information about any function of a module


print(m.nan, type(m.nan))


#importing a module in same directory as your current script

# from harry import welcome, harry
#from harry import *
import harry as hr

# welcome() 
hr.welcome()
# print(harry) 
print(hr.harry)






