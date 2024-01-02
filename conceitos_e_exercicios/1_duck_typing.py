"""
Duck typing:
'Se nada como um pato, se faz quack quack como um pato, então é um pato'
No python este é o tipo de tipagem adotada, que define que o que faz uma classe não é um nome especifíco, e sim a presença de determinados metódos e atributos nessa

É um conceito onde a linguagem não está interessada em um nome fixo para definir oque é uma classe/tipo, e sim interessado na presença dos metódos e atributos que compõem essa classe

Por exemplo eu posso criar um class de nome "Magic1" que tenha os mesmos metódos e atributos da classe str, e por isso os objetos instaciados na classe Magic1 vão ser considerados strings, pela presença dos metódos e atributos que fazem a classe str

Magic1 == str

Então um usuário se tiver o interesse, pode trocar as classes str, int e etc por classes próprias que tenham os metódos e atributos das classes anteriores
"""
