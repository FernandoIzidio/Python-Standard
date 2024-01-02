"""
Serialização - é o processo responsável por converter um objeto ou extrutura de dados em um formato que possa ser armazenado, transmitido, e posteriormente reconstruido em sua forma original

Armazenar, transmistir, reconstruir

Serialização : A serialização geralmente envolve o processo de conversão de objetos ou extruturas de dados em um formato serializado, geralmente uma sequência de bytes.

Desserialização: Processo inverso, é o processo de converter um objeto serializado, ou seja um sequência de bytes, em seu estado original

Formatos de serialização de dados:
    Json
    XML
    YAML
    Bson
    MessagePack
    Pickle - Serializa um objeto extrutura de dados, para o formato binário, porém esse formato só funciona em sistemas que adotem a linguagem python, é util para persistência de dados, e aplicações simples que não necessitem interoperabilidade e transmissão de dados entre diferentes linguagens.
    Obs: O pickle por serializar objetos e extruturas no formato binário. Pode ser usado para transmissão de dados em rede, somente entre sistemas que utilizem python.


Vantagens da serialização:

    Interoperabilidade - Permite que os dados possam operar e ser usados em diferentes sistemas e linguagens de programação, um exemplo é um dado/objeto serializado em json, que pode ser reconstruido com integridade em qualquer linguagem

    Armazenamento e Transmissão de dados - A serialização é um processo que facilita muito na armazanagem de dados em bancos de dodas, arquivos, e memória não volatil, também facilita muito na transmissão de dados entre redes

Desvantagens:
    Segurança: A deserialização de objetos, pode apresentar riscos, se vir de fontes não confiaveis, e o processo de desserialização permita a inclusão de código executavel


__reduce__ - dundermethod responsável por personalizar a serialização de objetos python, esse metódo é usado para definir como um objeto é serializado e deserializado, é muito util para salvar objetos em arquivos

def __reduce__(self):
     Retorna uma tupla com até cinco elementos
    return (func, args, state, iterator, extras)

    func - responsável por retornar um instância do objeto a ser serializado, esse é responsável pela deserialização

    *args - argumentos que serão passados para a função durante a deserialização, e criação do objeto

    state: Uma tupla ou outro objeto que representa o estado interno do objeto a ser serializado. Isso pode incluir informações adicionais que não são passadas como argumentos para o construtor.

    iterator (opcional): Um iterador que produz itens que serão inseridos no objeto durante a reconstrução. Este é um elemento opcional na tupla.

    extras (opcional): Outros dados que podem ser incluídos na tupla, se necessário.


No entando é incomum usar o __reduce__ para fazer serialização e deserialização, é mais comum usar o módulo pickle que faz serialização para binário de forma automática.

"""