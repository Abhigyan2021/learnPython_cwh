
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

filesMatched = 0 # Initialize filesMatched as 0

#Function to search the keyword in a given directory
def search_files(keyword, path):
    filesFound = filesMatched
    for root, dirs, files in os.walk(path): # use os.walk(path) to loop through the given directory  and get the root, dirs, and files
        for file in files : # Loop through all the files in the given directory
            if keyword in file: # Check if keyword is in filename
                filesFound += 1 # Counter to see how many files matched
                print(" " + root + "\\" + str(file) + "\n") # Print out the full file path for every matching file
                if filesFound == 0 : #check if no files matched the given keyword and print the same
                    print("No matching files in the given directory! Try another directory!")

    # If 1 or more files are matched then print the same.
    print(f"No. of files matched : {filesFound}")

try:
    search_files(keyword, path) # Call the function
# Error and Exception Handling
except FileNotFoundError as e:
    print("Error: FileNotFoundError Occurred! Make sure you entered the correct path and entered it correctly.")
except Exception as e:
    print(f"Error: Some Error occured! \nDetails: {e}")
