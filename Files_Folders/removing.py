from pathlib import Path
import shutil 
import os
import send2trash

#os.unlink(Path.home() / Path("OneDrive", "Desktop", "New folder", "afteredit.txt"))
#os.rmdir(Path.home() / Path("OneDrive", "Desktop", "New folder", "empty"))

#shutil.rmtree(Path.home() / Path("OneDrive", "Desktop", "New folder", "myfolder"))

send2trash.send2trash(Path.home() / Path("OneDrive", "Desktop", "New folder", "myfolder"))
send2trash.send2trash(Path.home() / Path("OneDrive", "Desktop", "New folder", "myfile.txt"))