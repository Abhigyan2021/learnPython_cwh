
## Code for handling FILE IO in python

# Tags - r for read, w for write , a for append, x creates file and creates error if file already exists


#Reading Files


# 'r' is default
# we can use 'rt' for reading txt file or 'rb' for binary files , jpg etc.

f = open('myfile.txt', 'r')
print(f) # prints <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='cp1252'>

text = f.read()
print(text)
f.close()


# Writing File


# we can also create file using 'w' mode

f = open('myfile2.txt', 'w')
f.write("Hello, World!")
f.close()

# It is important to close the file without it write function won't work

# Another method to open or close the file - with keyword

# Appending a file 


with open('myfile.txt', 'a') as f:
    f.write("\nHey I am inside the first file!")


# Readline Method


f = open('myfile.txt', 'r')

while True:
    line = f.readline()
    if not line:
        break
    print(line)

f.close()


with open('mymrk.txt', 'r') as f:
    i = 0

    while True:
        i = i + 1
        line = f.readline()

        if not line:
            break
        
        #NOTE : m1,m2,m3 is a string and not an integer

        m1 = line.split(",")[0]
        m2 = line.split(",")[1]
        m3 = line.split(",")[2]

        print(f"Marks of student {i} in Maths is: {m1}")
        print(f"Marks of student {i} in English is: {m2}")
        print(f"Marks of student {i} in SST is: {m3}")

        print(line)


# writeline method


#NOTE : Write line method doesn't add a newline itself

f = open("myfile2.txt", 'w')

lines = ['line1\n', 'line2\n', 'line3\n']

f.writelines(lines)
f.close()


#SEEK,TELL & TRUNCATE - Performing operations at selected positions in file


#seek is used to go at certain position in text
#tell is used to get information about the position we're at
#truncate is used to limit the size of file to a certain number of characters


with open('myfile.txt','r') as f:
    print(type(f))

    f.seek(24)

    while True:
        
        line = f.readline()
        print(f.tell())
        if not line:
            break
        print(line)


with open('smpl1.txt','w') as f:
    f.write('Hello World!')
    f.truncate(5)

with open('smpl1.txt', 'r') as f:
    print(f.read())




