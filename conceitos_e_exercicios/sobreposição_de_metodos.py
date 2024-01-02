"""
Para executar metódos de mesmo nome das parents class, mesmo que esse metódo exista na child class, é usado a class super().nomedometodo para executar o metódo de uma parent class

super().method
Executa um metódo de uma parent class, passando o objeto e atributos atuais como argumentos do metódo da parent class

super(class, self).method - Executa o metódo na parent class informada, passando o objeto e atributos atuais como argumentos para a parent class
"""

class SMS:
    def __init__(self, conteudo:str, user:str) -> None:
        self.conteudo = conteudo
        self.user = user

    def enviar_mensagem(self, endereco:str, horario:int):
        print(f'{self.conteudo}')
        print(f'Mensagem de {self.user} enviada com sucesso para {endereco} ás {horario}Hrs por SMS')


class Whatssap(SMS):
    def __init__(self, numero,  conteudo: str, user: str) -> None:
        super().__init__(conteudo, user)
        self.numero = numero

    def enviar_mensagem(self, endereco:str, horario:int):
        super().enviar_mensagem(endereco, horario)
        print('') 
        print(f'{self.conteudo}')
        print(f'Mensagem de {self.user} enviada com sucesso para {endereco} ás {horario}Hrs por Whatsapp')       


num = Whatssap(89841474152, 'Bom dia Jamelão', "Carlão48")

num.enviar_mensagem('Jamelão', 18)