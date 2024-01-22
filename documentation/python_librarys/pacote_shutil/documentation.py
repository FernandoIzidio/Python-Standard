"""
shutil(shell utilitys) é usado para realizar operações de alto nivel em arquivos e diretórios

Metódos uteis:
    shutil.copyfileobj - Copia o conteudo de um arquivo para um filedescriptor

    shutil.copyfile(src, dst, *, follow_symlinks=True) - Copia apenas o conteúdo do arquivo, ignorando data de criação e outros metadados
    
    shutil.copymode(src, dst, *, follow_symlinks=True) - Copia as mascaras de permissões octais de um arquivo para o outro

    shutil.copystat(src, dst, *, follow_symlinks=True) - Copia mascara de permissão octal, e metadados do aruivo par aum outro arquivo

    
    copy - Copia o arquivo de um diretorio para outro

    move - Move um diretório e seus subdiretorios e arquivos para dentro de um outro diretorio, pode renomear diretórios e arquivos

    copytree - Copia recursivamente todos os arquivos e subdiretórios de um caminho para ou outro
    
    rmtree - Remove recursivamente todos os subdiretórios e arquivos de um caminho 



"""
