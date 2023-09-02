import shutil
from pathlib import Path

shutil.copy(Path.home() / Path("OneDrive", "Desktop", "New folder", "File_one.txt"), Path.home() / Path("OneDrive", "Desktop", "New folder", "copy", "file_one_copied.txt"))
shutil.copytree(Path.home() / Path("OneDrive", "Desktop", "New folder"), Path.home() / Path("OneDrive", "Desktop", "New folder", "folder"))