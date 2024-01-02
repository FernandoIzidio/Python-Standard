from pathlib import Path
import os, shutil
WORK_FOLDER = Path(__file__).parent / "Python-Standard"

table = str.maketrans(" ", "_")

for currentdir, subdir, filename in os.walk(str(WORK_FOLDER)):
    
    for file in filename:
        wayfile = Path(os.path.join(currentdir, file))
        shutil.move(wayfile.__str__(), wayfile.__str__().translate(table))
        
    for directory in subdir:
        waysdir = Path(os.path.join(currentdir, directory))
        shutil.move(waysdir.__str__(), waysdir.__str__().translate(table))
        
    

        

        


