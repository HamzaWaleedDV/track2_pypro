from pathlib import Path

myfile = open('file_one.txt', "a")
myfile = open(Path.home() / Path("OneDrive", "Desktop", "New folder", "File_one.txt"), "w")

myfile.write('11. Hello how are you')
myfile.write('12. Hello how are you')
myfile.write('13. Hello how are you')

# words = ['\n14. Hello how are you\n', '15. Hello how are you\n', '16. Hello how are you\n']

# myfile.writelines(words)