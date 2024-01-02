import os, pathlib, zipfile
class Manager_Venv:
    def __init__(self) -> None:
        self.workdir = pathlib.Path(os.getcwd())

    def create_file(self, relativepath:str|pathlib.Path=None):
        if relativepath:
            (self.workdir / relativepath).touch(exist_ok=True)
        else:
            (self.workdir / 'temp').touch(exist_ok=True)


    def create_folder(self, relativepath:str|pathlib.Path=None):
        if relativepath:
            (self.workdir / relativepath).mkdir(exist_ok=True)
        else:
            (self.workdir / 'FolderTemp').mkdir(exist_ok=True)

    def extract_zip(self, file:str|pathlib.Path, target_relative_folder: str|pathlib.Path):
        try:
            with zipfile.ZipFile(file, 'r') as file:
                file.extractall(target_relative_folder)
        except Exception as Error:
            raise Error


    def compress_folder(self, namezip:str|pathlib.Path, folder_to_compress:str|pathlib.Path):
        global zipfile    
        try:
            
            contextzip = zipfile.ZipFile((self.workdir / namezip).__str__(), 'w')
            
            with contextzip as zipfile:
                for currentdir, subdirname, filename in os.walk((self.workdir / folder_to_compress)):
                    if filename:
                        for file in filename:
                            zipfile.write(os.path.join(currentdir, file), pathlib.Path(os.path.join(currentdir, file)).relative_to(os.getcwd()))
        
        except Exception as error:
           raise error

