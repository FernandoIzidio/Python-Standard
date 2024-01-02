from abc import abstractclassmethod
from copy import copy
from typing import Any, Union
from os import system, path
from time import sleep
from pandas import DataFrame, ExcelWriter
from openpyxl.styles import PatternFill, Font
from decimal import Decimal

def implementa_senha_desconto_e_construtor(percent, senha):
    def modifica_class(cls):

        @property
        def metodo_senha(self) -> Any:
            return senha
        
        @property
        def metodo_desconto(self)-> Decimal:
            return Decimal(percent)
        
        @classmethod
        def gerar_anonimo(cls, nivel):
            return cls('Anônimo', 'Desconhecido', nivel)


        cls.senha:Any = metodo_senha
        cls.desconto:float = metodo_desconto
        cls.geraranom = gerar_anonimo
        return cls
    return modifica_class

def input_numerico(msg, classe: Union[int, float, Decimal], func=None, *args) -> Union[int, float, Decimal]:
     while True:
        try:
            system('clear')
            if func != None:
                func(*args)

            valorinformado = classe(input(msg))
        except Exception as error:
            print('Digite apenas números')
            sleep(1.5)
        else:
            return valorinformado


class Sistema_de_Desconto:
    def __init__(self) -> None:
        self.funcionarios = [Vendedor.geraranom('Operacional'), Gerente.geraranom('Estratégico'), Supervisor.geraranom('Tático')]
        self.login = False
        self.currentuser: Funcionario = None
        self.soma = 0
        
        
    def solicitar_senha(self):
        self.senhainformada = input('Informe a senha:')

    def autenticar(self):
        funcionarioesc = []
        if any(self.senhainformada == funcionario.senha and (funcionarioesc.append(funcionario) or True) for funcionario in self.funcionarios):
            self.login = True
            self.currentuser = funcionarioesc[-1]
            self.currentuser.lista = []
    
    def deslogar(self):
        self.login = False

    def adicionar_produto(self):
        system('clear')
        self.nomeproduto = input('Informe o nome do produto: ')
        produtoesc = []
        if any(self.nomeproduto == dicionario['Nome'] and (produtoesc.append(dicionario) or True) for dicionario in self.currentuser.lista):
            dicionarioesc = produtoesc[-1]
            temp = input_numerico('Digite o número de produtos a mais: ', int)
            dicionarioesc['Quantidade'] += temp
            dicionarioesc['Valor Total'] = (dicionarioesc['Preco/Uni'] * dicionarioesc['Quantidade'])
            self.soma += (dicionarioesc['Preco/Uni'] * temp)
        else:

            self.valor = input_numerico('Informe o valor do produto: ', Decimal)
            self.quantidade = input_numerico('Informe a quantidade: ', int)
            self.total = self.valor * self.quantidade
            self.currentuser.lista.append({'Nome': self.nomeproduto, 'Quantidade': self.quantidade,'Preco/Uni': self.valor ,'Valor Total': self.total, 'Status': Decimal(0), 'Valor Retroativo': self.total})
            self.soma += self.total

    def listar_produtos(self, flag_visual = False):
        system('clear')
        if self.currentuser.lista:
            
            print('='*50)
            for pos, produto in enumerate(self.currentuser.lista):
                print(f'{f"Produto {pos+1}":^50}')
                print('-'*50)
                for chave, valor in produto.items():
                    if chave not in ('Status', 'Valor Retroativo'):
                        print(f'{chave}: {valor}' if chave not in ('Valor Total', 'Preco/Uni') else f'{chave}: R${valor:.2f}'.replace('.', ','))
                print('-'*50)
            print(f'Valor a pagar: R${self.soma:.2f}'.replace('.',','))
            print('='*50)
            if not flag_visual:
                input('')
        else:
            print('Nada a listar')
            input('Next:')

    def remover_produtos(self):
        system('clear')
        if self.currentuser.lista:
            while True:
                system('clear')
                userpos = input_numerico('Digite a posição do produto: ', int, self.listar_produtos, True) - 1

                if userpos in range(len(self.currentuser.lista)):
                    while True:
                        system('clear')
                        opt3 = input('Digite:\nT - Para remover todos os produtos selecionados\nQ - Para remover uma quantidade de produtos\n:').upper()
                        if opt3 in ('T', 'Q'):
                            break
                        print('Digite uma opção válida')
                        sleep(1.5)

                    match opt3:
                        case 'T':
                            self.soma -= self.currentuser.lista[userpos]['Valor Total']
                            self.currentuser.lista.pop(userpos)
                            
                        case 'Q':
                            system('clear')
                            val = input_numerico('Informe a quantidade que deseja remover:', int)
                            self.currentuser.lista[userpos]['Quantidade'] -= val
                            if self.currentuser.lista[userpos]['Quantidade'] <= 0:
                                self.soma -= self.currentuser.lista[userpos]['Valor Total']
                                self.currentuser.lista.pop(userpos)
                                print('Todos os items removidos com sucesso')
                            else:
                                self.currentuser.lista[userpos]['Valor Total'] -= (val * self.currentuser.lista[userpos]['Preco/Uni'])
                                self.soma -= (val * self.currentuser.lista[userpos]['Preco/Uni'])
                                print(f'{val} items removidos com sucesso.')
                                
                            input('')
                    break
                print('ERRO: Digite uma opção válida!!!')
                sleep(1.5)
        else:
            print('Nada a remover')
            input('Next:')

    def solicitar_desconto(self):
        system('clear')
        if self.currentuser.lista and not all(dicionario['Status'] == 1 for dicionario in self.currentuser.lista):

            self.descontoinformado = input_numerico('Informe a % de desconto da compra[0,100]: ', Decimal)

            if any(self.descontoinformado/((self.currentuser.desconto * 100)) + produto['Status'] <= 1 for produto in self.currentuser.lista) and self.descontoinformado <= 20:
                self.currentuser.lista = [{**produto, 'Valor Total': produto['Valor Total'] -(produto['Valor Retroativo'] * self.descontoinformado)/100, 'Status': ((produto['Status'] + (self.descontoinformado)/(self.currentuser.desconto * 100)))} if ((self.descontoinformado / (self.currentuser.desconto * 100)) + produto['Status']) <= 1 else {**produto} for produto in self.currentuser.lista]

                self.soma = sum(list(produto['Valor Total'] for produto in self.currentuser.lista))
                print(self.soma)

                print('Desconto aplicado com sucesso')
                self.listar_produtos(True)
                input('Next:')
            else:
                print(f'Desconto permitido: até {self.currentuser.desconto * 100:.2f}%')
                print(f'Erro: Você não pode aplicar um desconto maior que {self.currentuser.desconto * 100:.2f}%!')
                input('Next:')
        else:
            print('Nada a aplicar desconto/ou Desconto já aplicado em todos produtos')
            input('Next:')
            
    def informar_dados(self):
        system('clear')
        print('='*50)
        print(f'{"Dados de Usuário":^50}')
        print('='*50)
        print(f'Nome: {self.currentuser.nome}')
        print(f'Sálario: R${self.currentuser.salario:.2f}'.replace('.',',') + '.')
        print(f'Cargo: {self.currentuser.__class__.__name__}')
        print(f'Nivel: {self.currentuser.nivel}')
        print('='*50)
        input('Next:')

    def salvar_dados(self):
        global opt
        system('clear')

        if self.currentuser.lista:
            while True:
                wayfile, extensao = path.splitext(input('Informe o caminhho/nome do arquivo[-1 aborta]:'))
              
                if '-1' in wayfile:
                    break

                try:
                    datauser = {
                        'Nome': self.currentuser.nome,
                        'Sálario': f'R${self.currentuser.salario:.2f}'.replace('.',','),
                        'Cargo': self.currentuser.__class__.__name__,
                        'Nível': self.currentuser.nivel,
                        'Valor das Compras': f'R${self.soma:.2f}'.replace('.',',')
                    }

                    userproducts = [{**dicionario, 'Preco/Uni': f'R${dicionario["Preco/Uni"]:.2f}'.replace('.', ','), 'Valor Total': f"R${dicionario['Valor Total']:.2f}".replace('.',',')} for dicionario in self.currentuser.lista]

                    userproducts = [{chave: valor for chave, valor in dicionario.items() if chave not in ('Valor Retroativo', 'Status')} for dicionario in userproducts]
                    
                    datauser = DataFrame(datauser, index=[0])
                    userproducts = DataFrame(userproducts)

                    with ExcelWriter(wayfile + '.xlsx', engine='openpyxl') as excelsheets:
                        datauser.to_excel(excelsheets, index=False, sheet_name='Dados Usuário', startrow=0, startcol=0)
                        userproducts.to_excel(excelsheets, index=False, sheet_name='Lista de Produtos', startrow=0, startcol=0)

                        woorkbook = excelsheets.book
                        user_sheet = excelsheets.sheets['Dados Usuário']
                        product_sheet = excelsheets.sheets['Lista de Produtos']

                        background = PatternFill(fill_type='solid', fgColor='00FF00')  
                        letter_font = Font(color='FFFFFF', bold=True)

                        for celula in user_sheet[1]:
                            if celula.value:
                                celula.fill = background
                                celula.font = letter_font
                                

                        for celula in product_sheet[1]:
                            if celula.value:
                                celula.fill = background
                                celula.font = letter_font
                        
                except Exception as error:
                    print('Arquivo/Diretório invalido')
                    print(error)
                    raise error
                else:
                    input('Arquivo salvo com sucesso.\nNext:')
                    self.login = False
                    opt = '2'
                    break
        else:
            print('Nada a salvar!')
            input('Next:')


class Funcionario:
    def __init__(self, nome:str, salario:float|Decimal, nivel:str) -> None:
        self.nome = nome
        self.salario = salario
        self.nivel = nivel
        
    @property
    @abstractclassmethod
    def senha(self):...

    @property
    @abstractclassmethod
    def desconto(self):...

@implementa_senha_desconto_e_construtor(0.05, 'vend123')
class Vendedor(Funcionario):...


@implementa_senha_desconto_e_construtor(0.10, 'sup456')
class Supervisor(Funcionario):...


@implementa_senha_desconto_e_construtor(0.20, 'ger789')
class Gerente(Funcionario):...

def log_client(attempt_current:int):
    global opt
    if attempt_current >= 5:
        system('clear')
        print('Limite de tentativas excedido.')
        print('Não possui permissão para acessar o sistema')
        input(':')    
        opt = '2'
        return
    
    system('clear')
    system_.solicitar_senha() 
    system_.autenticar()
    system('clear')
    if system_.login:
        system_.currentuser.nome = input('Digite seu nome: ')
        system_.currentuser.salario = input_numerico('Informe o seu sálario: ', float)
        return

    print('ERRO: Digite uma senha válida')
    sleep(1.5)
    return log_client(attempt_current+1)

opt = ''
system_= Sistema_de_Desconto()
while True:
    if not system_.login:   
        if opt == '2':
            system('clear')
            print('Encerrando...')
            break

        actions = {'1': lambda: log_client(0)}
        
        system('clear')
        print('='*50)
        print(f'{"Sistema de Desconto":^50}')
        print('-'*50)
        print('[1] - Para Logar')
        print('[2] - Para Sair')
        print('-'*50)
        
        opt= input(':')
        userchoice = actions.get(opt)

        if userchoice != None:
            userchoice()
            continue
        elif not opt in ('1', '2'):   
            print('ERRO digite uma opção válida!')
            sleep(1.3)

    else:
        actions = {
            '1': lambda: system_.adicionar_produto(),
            '2': lambda: system_.listar_produtos(),
            '3': lambda: system_.remover_produtos(),
            '4': lambda: system_.solicitar_desconto(),
            '5': lambda: system_.informar_dados(),
            '6': lambda: system_.salvar_dados()
        }

        system('clear')
        print('='*54)
        print(f'{"Sistema de Desconto":^54}')
        print('-'*54)
        print(f'| [1] - {"Para adicionar produtos a lista de compras":<45}|')
        print(f'| [2] - {"Para mostrar produtos da lista de compras":<45}|')
        print(f'| [3] - {"Para remover produto da lista de compras":<45}|')
        print(f'| [4] - {"Para aplicar desconto nos produtos da lista":<45}|')
        print(f'| [5] - {"Para informar dados de usuário":<45}|')
        print(f'| [6] - {"Para salvar lista de compras e sair":<45}|')
        print(f'| [7] - {"Para deslogar da conta":<45}|')
        print('-'*54)
        opt2 = input(': ')

        userchoice = actions.get(opt2)
        if userchoice != None:
           userchoice()
           continue
        elif opt2 == '7':
            system('clear')
            print('Encerrando')
            system_.login = False
            continue



        