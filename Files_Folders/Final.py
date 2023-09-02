import os, re, shutil
from pathlib import Path

dataPattern = '^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)?\d\d)(.*?)$'

for filename in os.listdir(Path.home() / Path("OneDrive", "Desktop", "files")):
    search = re.search(dataPattern, filename)

    if search == None:
        continue

    beforepart = search.group(1)
    monthpart = search.group(2)
    daypart = search.group(4)
    yearpart = search.group(6)
    afterpart = search.group(8)

    newfilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart
    print(f'Renaming "{filename}" to "{newfilename}"')

    oldname = Path.home() / Path("OneDrive", "Desktop", "files") / filename
    newname = Path.home() / Path("OneDrive", "Desktop", "files") / newfilename
    shutil.move(oldname, newname)