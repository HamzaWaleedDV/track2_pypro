import os
from pathlib import Path

# print(os.getcwd())
# # os.chdir(r'E:\Back-End(hsoub)\Projects(Track 2)\Files_Folders')
# print(Path.home())

myfile = open(Path.home() / Path("OneDrive", "Desktop", "New folder", "File_one.txt"), "r")

# print(str(Path.home() / Path("OneDrive", "Desktop", "New folder", "File_one.txt")))

print(myfile)
print(myfile.name)
print(myfile.mode)

lines = myfile.readlines()
# print(lines[0:5])

print('-' * 50)
i = 0
for line in lines:
    print(line)

    i += 1

    if i == 5:
        break 

myfile.close()