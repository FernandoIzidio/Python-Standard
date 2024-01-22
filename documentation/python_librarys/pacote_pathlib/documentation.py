"""
Pathlib - Biblioteca útil para fazer manipulação de caminhos, e fazer os caminhos funcionarem tanto no windows, linux, max



pathlib:
    __file__ - Retorna caminho absoluto de um módulo

    PurePosixPath - Usado para tratar de caminhos em sistemas unix

    PureWindowsPath - Usado para tratar de caminhos em sistemas windows

    Path:
        -Todo objeto da classe path, tem como metódo str o caminho especificado 

        obj.absolute() - Retorna o caminho absoluto PARA o diretório/arquivo atual

        obj.parent - Retorna o caminho parent/ caminho acima do diretório atual

        Path.home() - Retorna o caminho para a pasta do usuário

        parts - Separa cada parte de um caminho em uma tupla

        drive - Retorna nome do disco/partição

        root - Retorna o delimitador de arquivos/diretórios

        anchor -  É uma concatenação da partição, com o delimitador

        parents - Retorna um iterator com todos caminhos de diretórios pais até a raiz

        name - Retorna o ultimo nome de um caminho, tipo os.path.basename

        suffix - Retorna a ultima extensão de um caminho, tipo os.path.splitext
        suffixes - Retorna todas as extensões de um caminho

        stem - Retorna o caminho sem o ultimo sufixo

        as_posix() - Retorna a representação unix de um caminho em unix-like
        as_uri() - Retorna a representação de um caminho no formato FTP
        is_absolute() - Verifica se um caminho está no formato absoluto
        is_relative_to(way)   - Verifica se o caminho atual pode ser relativo a outro caminho
        joinpath - Faz a mesma coisa que /, concatena caminhos
        match - Verifica se o caminho corresponde a um padrão

        path.relative_to(way) - Retorna um caminho relativo baseado no caminho informado 
        
        with_name(name) - Altera o ultimo nome de um caminho, ou seja altera o basename
        with_stem(name:str) - Altera o ultimo diretório/arquivo mas mantém a extensão




        pathobjeto.touch() - Cria um arquivo vazio, conforme o caminho informado no objeto
        pathobjeto.unlink() - Remove o arquivo
        pathobjeto.write_text('string') - Escreve conteudo no arquivo
        pathobjeto.read_text()->string - Retorna o conteúdo do arquivo
        pathobjeto.mkdir(exists_ok=bool) - Cria um diretório

        pathobjeto.isfile()->bool - Verifica se o objeto é um arquivo
        pathobjeto.isdir()-> bool - Verifica se o objeto é um diretório
        pathobjeto.exists() -> bool - Verifica se o diretório/arquivo existem 
        pathobjeto.glob(padraodebusca / *) -> iterator(Path) - Itera recursivamente sobre todos os subdiretórios e files de um caminho, e retorna um iterator contendo todos esses subdiretorio e files que correspondam ao padrão buscado, *pega todos os objetos Path de um caminho
        rename ou replace - Renomeia, move arquivo/diretório

        

        path.open(mode:str) - Abre o arquivo em algum modo escolhido, funciona como um context manager


        iterdir() - Retorna um iterator com o caminho de todos os subdiretorios, e arquivos de um caminho, iterdir() faz a mesma coisa que glob, porém glob, pode pesquisar apenas os subdiretorios que correspondam ao padrão

        glob funciona de forma semelhante ao walk, mas o walk itera de forma recursiva sobre todos subdirtorios e arquivos

        os.path.join(arg, arg, arg) - Cria um caminho usando os.
        path / arg / arg -  Cria um caminho usando a pathlib

        O processo de remoção de diretórios com arquivos, sempre é feito de forma recursiva

        """

from pathlib import Path
import json, faker

fk = faker.Faker(locale='pt_BR')

currentdir = Path(__file__).parent
print(currentdir.parts)
print(currentdir.drive)
print(currentdir.root)
print(currentdir.parents)
print(currentdir.joinpath("Truco"))
print(currentdir.relative_to(currentdir.parent.parent))

dirtest = currentdir / "DirTest"
dirtest.mkdir(exist_ok=True)
for num in range(1,11):
    (dirtest / f"Subdir{num}").mkdir(exist_ok=True)
    for num2 in range(1,10):
        file = (dirtest / f"Subdir{num}" / f"dados{num2}.json")
        file.touch(exist_ok=True)
        
        client_data = ({"Dados_Cliente" : {
            "Nome": fk.first_name(),
            "Sobrenome": fk.last_name(),
            "Idade": fk.random.randint(16, 73), 
            "Telefone": fk.phone_number(),
            "Email": fk.email(),
            "Endereço": fk.address()
        }, "Produtos_Comprados: ": {f"Produto {count}": f"R${round((fk.random.uniform(1, 100) * fk.random.uniform(1, 5)), 2):.2f}".replace('.', ',') for count in range(1, 11)}} for count in range(10))


        with file.open('w', encoding='utf-8') as jsonfile:
            json.dump(list(client_data), jsonfile, indent=2, ensure_ascii=False)


for way in dirtest.iterdir():
    print(way)

print("")
print(*dirtest.glob("*"), sep='\n')




