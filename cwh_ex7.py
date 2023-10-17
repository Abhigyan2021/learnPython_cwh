
# decluttering the folder with random names

import os

files = os.listdir("clutter")

#currently files are 
for file in files : 
    print(file)


'''
1017256-widescreen-american-muscle-car-wallpaper-1920x1080.jpg
1017380-popular-american-muscle-car-wallpaper-1920x1440-for-mac.jpg123650.png
1301601.jpg
1718884.jpg
5wunaspoq9n8ygax.jpg
6144758-fantasy-city-ballerina-blade-runner-cyberpunk-pink-blue-alex-feliksovich-luminos-buildings.jpg
67960.jpg
744722.png
76000-alien-logo-artist-artwork-digital-art-hd-4k.jpg

'''
print("\n\n")

#now we are going to rename files

i = 1 # --> to rename the files as numbers
#traversing the loop

for file in files :
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutter/{file}", f"clutter/{i}.png")
        i = i + 1
    elif file.endswith(".jpg"):
        print(file)
        os.rename(f"clutter/{file}", f"clutter/{i}.jpg")
        i = i+1
      
