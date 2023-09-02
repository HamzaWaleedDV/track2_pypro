import zipfile
from pathlib import Path
import os
import shutil

# compresszip = zipfile.ZipFile(Path.home() / Path("OneDrive", "Desktop", "New folder.zip"))

# print(compresszip.namelist())

# fileinfo = compresszip.getinfo('New folder/File_one.txt')
# print(fileinfo.file_size)

# print(fileinfo.compress_size)

#extract()
# os.chdir(Path.home() / Path("OneDrive", "Desktop"))
# compresszip.extract('New folder/style.css', Path.home() / Path("OneDrive", "Desktop", "extractfile"))

# #compress file
# new_zip = zipfile.ZipFile('new.zip', 'w')
# new_zip.write('New folder/File_one.txt')

#compress folder
# folder_zip = zipfile.ZipFile('new_folder.zip', 'w')
# folder_zip.write(Path.home() / Path("OneDrive", "Desktop", "New folder"))


shutil.make_archive('compressFolder', 'zip', Path.home() / Path("OneDrive", "Desktop", "New folder"))