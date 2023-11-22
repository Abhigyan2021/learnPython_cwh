
# Shutil Module - Performs high level file operations such as copying, moving a file.

#NOTE : Run the below commands only one at a time

import shutil
import os

#1 -- copying a file

# shutil.copy("cntr1.txt", "txts/cntr3.txt")

#2 -- copying a folder

# shutil.copytree("txts", "txts2")

#3 -- Moving a Folder

# shutil.move("txts/cntr3.txt", "cntr3.txt")

#4 -- Deleting a Folder

# shutil.rmtree("txts")
# shutil.rmtree("txts2")

#5 -- Removing the copied file

# os.remove("cntr3.txt")