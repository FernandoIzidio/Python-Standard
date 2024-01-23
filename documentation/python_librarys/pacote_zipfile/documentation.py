"""
ZipFile(file.zip, mode) - É um context Manager para criar arquivos zip

    zp.write(absoluteway, relativeway) - Adiciona um arquivo, ao arquivo zip
    zp.namelist() - Retorna todos os arquivos do zip
    zp.extractall(way) - Descompacta arquivo zip

Obs: Usar sempre caminhos relativos
 """
from pathlib import Path
import faker, os
from zipfile import ZipFile
from shutil import make_archive
waydir = Path(__file__).parent
fk = faker.Faker('pt_BR')
myzipfile = (waydir / "arquivo.zip")
myzipfile.touch()

directory = waydir / "Directory"
directory.mkdir(exist_ok=True)

for count in range(1, 11):
    subdir = (directory / f"Subdir{count}")
    subdir.mkdir(exist_ok=True)

    for count in range(1, 11):
        file = subdir / f"File{count}.txt"
        #file.touch(exist_ok=True)
        #file.write_text(faker.Faker().text())



with ZipFile(myzipfile, 'w') as zipfile:
   
   for currentway, subdirname, filename in os.walk(directory.__str__()):
       if filename:
           for file in filename:
               zipfile.write(os.path.join(currentway, file), Path(os.path.join(currentway, file)).relative_to(waydir))
    


with ZipFile(myzipfile, 'r') as zipfile:
    zipfile.extractall(waydir / "Directory 2")