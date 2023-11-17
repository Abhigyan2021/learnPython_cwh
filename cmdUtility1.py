
#This is a small example project of command line utility 

#This project is made by studying from the article at this link : https://dev.to/pybash/how-to-create-a-command-line-utility-using-python-4ae6

#search.py -CLI Utilities

try:
    import os #stdlib
    import sys # stdlib
except ImportError as e:
    print("Error : Some modules could not be imported from stdlib('sys' and 'os')")

keyword = sys.argv[1] #Get the keyword that is to be searched for
path = " ".join(sys.argv[2:]) #Get the path where to search for the keyword

