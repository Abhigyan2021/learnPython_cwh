
#Using basic functions of os module

import os

# if(not os.path.exists("data")):    
#     os.mkdir("data") # If we don't use a check here it will cause error


# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")


# If after making 100 folders we want to rename it, we can do it following way:

# for i in range(0,100):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial {i+1}")


# for finding the name of folders

# folders = os.listdir("data")

# print(folders) #this prints a list of folders


# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))


#os.system module


# cmd = 'date'

# os.system(cmd)


# Traversing directory


# print(os.getcwd()) #get current working directory
# os.chdir("/Django Development")#change directory
# print(os.getcwd())






