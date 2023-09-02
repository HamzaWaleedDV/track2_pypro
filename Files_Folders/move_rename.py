from pathlib import Path
import shutil

shutil.move(Path.home() / Path("OneDrive", "Desktop", "New folder", "Beforeedit.txt"), Path.home() / Path("OneDrive", "Desktop", "New folder", "afteredit.txt"))