
from abc import abstractclassmethod, ABC
from os import system
from time import sleep
from random import randint
from dataclasses import dataclass, field
sistema = {'Bancos': []}

def implementa_sacar(cls):
    class ContaBancaria(cls):
        def _sacar(self, money):
            if (self.saldo - money >= self.limite) and money > 0:
                self.saldo -= money
                self.dadoscliente.dinheirobolso += money
                print(f'Saque de R${money:.2f} realizado com sucesso'.replace(".", ",") + '.')
                print(f'Saldo: R${self.saldo:2f}'.replace('.', ','))
                return self.saldo
            print('Saque negado!!!')
            print('Exp: Não possui saldo/crédito o suficiente para realizar operação')
    return ContaBancaria


class Conta(ABC): 
    def __init__(self, agencia: int, numero: int, senha: int, saldo: float | int = 0) -> None: 
        super().__init__()
        self.agencia:int = agencia
        self.numero:int = numero
        self.saldo:float = saldo
        self.senha:int = senha
        self.banco:Banco = None
        self.dadoscliente:Cliente = None
        self.limite = 0

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Conta):
            cond1 = self.agencia == other.agencia
            cond2 = self.numero == other.numero
            cond3 = self.saldo == other.saldo
            return (cond1 and cond2 and cond3)
        return False
    
    def transferir(self, numero, dinheiro):
        other = []
        if any(list(numero == contab.numero and (other.append(contab) or True) for banco in sistema['Bancos'] for contab in banco.listaconta)) and dinheiro > 0 and (self.saldo - dinheiro >= self.limite):
            self.saldo -= dinheiro
            contab: Conta = other[-1]
            contab.saldo += dinheiro
            print('='*50)
            print('Operação realizada com sucesso')
            print('-'*50)
            print(f'Valor da operação: {dinheiro:.2f}'.replace('.', ',') + '.')
            print(f'Saldo do Pagante({self.dadoscliente.nome}): R${self.saldo:.2f}'.replace('.', ',') + '.')
            print(f'Saldo do Beneficiário({contab.dadoscliente.nome}): R${contab.saldo:.2f}'.replace('.', ',') + '.')
            print('='*50)
            return ''
        print('ERRO: /Não possui dinheiro o suficiente para operação ou número invalido')

    @abstractclassmethod
    def _sacar(self): ...

    def depositar(self, dinheiro):
            if self.dadoscliente.dinheirobolso >= dinheiro and dinheiro > 0:
                self.dadoscliente.dinheirobolso -= dinheiro
                self.saldo += dinheiro
                print(f'Deposito de R${dinheiro:.2f} realizado com sucesso'.replace(".", ",") + '.')
                print(f'Saldo: R${self.saldo:2f}'.replace('.', ','))
            else:
                print(f'Dinheiro em carteira: {self.dadoscliente.dinheirobolso}')
                print(f'Não possui dinheiro suficiente para operação.')


@implementa_sacar
class ContaCorrente(Conta):   
    def increase_limite(self):
        self.limite = 0 - (self.dadoscliente._renda * 0.50)
        print(f'Novo limite da conta: {self.limite}')
        return self.limite

@implementa_sacar
class ContaPoupanca(Conta):...


@dataclass
class Pessoa:
    _nome: str
    _idade: int
    _id: int
    _renda: float
    dinheirobolso = 0
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Pessoa):
            cond1 = self._nome == other._nome
            cond2 = self._idade == other._idade
            cond3 = self._id == other._id
            return (cond1 and cond2 and cond3)
        return False

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

@dataclass
class Cliente(Pessoa):
    conta: list[Conta] = field(default_factory=list)

@dataclass
class Banco:
        nome : str
        agencias : list[int] = None
        listaclientes : list[Cliente] = None
        listaconta : list[Conta] = None
        contaclient: Cliente = None 
        
        def registrar_conta(self, cliente:Cliente, conta:Conta):
            self.listaclientes.append(cliente)
            self.listaconta.append(conta)

def input_int(num:int, msg:str, flagvisual:bool = False, func=None, *args) -> list[int]:
    data = []
    while not len(data) >= num:
        while True:
                if not flagvisual:
                    system('clear')
                if func != None:
                    if args:
                        func(*args)
                    else:
                        func()
                print('='*50)
                try:
                    number = int(input(msg))
                    print('-'*50)
                except (TypeError, ValueError):
                    print('ERRO: Digite apenas números inteiros.')
                    sleep(1)
                    system('clear')
                else:
                    if number not in data:
                        data.append(number)
                        break
                    print('ERRO: Não digite números repetidos')
                    sleep(1)
                    system('clear')
                print('='*50)   
    return data

def validar_cpf(cpf:int) -> bool:
    cpf = str(cpf)
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[10]):
        return False
    return True

def input_float(msg) -> float:       
    while True:
        system('clear')
        print('='*50)
        try:
            data = float(input(msg))
            print('-'*50)
        except (TypeError, ValueError):
            print('ERRO: Digite apenas números.')
        else:
            break
        print('='*50)
    return data       


def valida_cpf(msg:str)-> int:
    while True:
        identidade = input_int(1, msg)[0]

        if  validar_cpf(identidade):
            return identidade

        print('ERRO: Digite um cpf válido.')
        sleep(1)


def informar_dados()->Cliente| bool:
    while True:
        system('clear')
        print('='*50)
        nome = input('Digite seu nome:').capitalize().strip()
        if nome:
            break
        print('ERRO: Nome não pode ser vazio')
        sleep(1)

    idade = input_int(1, 'Digite sua idade:')[0]
    if idade < 0:
        idade = -idade

    renda = input_float('Informe renda média mensal:')

    while True:
        system('clear')
        clientecheck = []
        identidade = valida_cpf('Informe seu cpf [12345678909 para abortar]:')
        
        if identidade == 12345678909:
            print('Abortando...')
            input('Next: ')
            return False
        
        currentclient = Cliente(nome, idade, identidade, renda)
        
        if all(list(not((clientecheck.append(cliente) or True) and currentclient._id == cliente._id) for banco in sistema['Bancos'] for cliente in banco.listaclientes)):
            clientecheck.clear()
            return currentclient
        else:
            if currentclient.nome == clientecheck[-1].nome and currentclient.idade == clientecheck[-1].idade:
                return clientecheck[-1]

        
            
        print('ERRO: CPF pertence a outra pessoa')
        input('Next: ')


def dados_conta(cliente: Cliente):
    print('='*50)
    print(f'{Bancologin.nome:^50}')
    print('='*50)
    print(f'Número da conta: {Contalogin.numero}')
    print(f'Tipo de conta: {Contalogin.__class__.__name__}.')
    print(f'Agência da conta: {Contalogin.agencia}')
    print(f'Nome do cliente: {cliente.nome}.')
    print(f'Idade do cliente: {cliente.idade}.')
    print(f'Cpf do cliente: {str(cliente._id)[:3]}.{str(cliente._id)[3:6]}.{str(cliente._id)[6:9]}-{str(cliente._id)[9::]}')
    print(f'Saldo da conta R${Contalogin.saldo:.2f}'.replace('.', ',')+ '.')
    print(f'Limite da conta: R${Contalogin.limite:.2f}'.replace('.', ',') + '.')
    print(f'Dinheiro em carteira: R${cliente.dinheirobolso}'.replace('.', ',') + '.')
    print(f'Renda média do cliente: R${cliente._renda}'.replace('.', ','))
    print('='*50)


def consulta_Banco() -> None:
    system('clear')
    if sistema['Bancos']:
        print('='*50)
        print(f'{"Bancos":^50}')
        print('-'*50)
        for pos, banco in enumerate(sistema['Bancos']):
            print(f'{pos+1} - {banco.nome}')
        print('='*50)
        sleep(1)
        return None
    
    print('Nenhum banco registrado no sistema.')
    input('Next:')


def seleciona_banco() -> Banco| None:
    system('clear')
    if sistema['Bancos']:
        while True:
            system('clear')
            bancoesc = input_int(1, 'Selecione um número de Banco: ', True, consulta_Banco)[0] - 1
            if bancoesc in range(len(sistema['Bancos'])):
                return sistema['Bancos'][bancoesc]
            print(f'ERRO: Digite um número no intervalo de {1} a {len(sistema["Bancos"])}')
            sleep(1)
            
            
    print('Nenhum banco registrado no sistema')
    input('Next: ')


def consulta_Agencia(banco: Banco) -> None:
    system('clear')
    print('='*50)
    print(f'{f"Agências do {banco.nome}":^50}')
    print('='*50)
    for pos, agencia in enumerate(banco.agencias):
        print(f'{pos+1} -  {agencia}')
    print('='*50)    
    sleep(1)
    

def seleciona_agencia(banco: Banco) -> int:
    while True:
        agenciaesc = input_int(1, 'Selecione o número da agência:', True, consulta_Agencia, banco)[0] - 1
        if agenciaesc in range(len(banco.agencias)):
            return banco.agencias[agenciaesc]
        print(f'Erro: digite um número no intervalo de {1} a {len(banco.agencias)}.')
        sleep(1.5)
        system('clear')


def set_passwd(msg, abortar =  False) -> int:
    while True:
        system('clear')
        senha = input_int(1, msg)[0]
        if len(str(senha)) == 6 and senha != 111111 or senha == 111111 and abortar:
            break
        print('ERRO: A senha deve ter 6 digitos numéricos')
        sleep(1)
    return senha


def criar_conta() -> Conta:
    system('clear')
    if sistema['Bancos']:
        cliente = informar_dados()
        if cliente:
            banco = seleciona_banco()
            agencia = seleciona_agencia(banco)

            while True:
                system('clear')
                print('='*50)
                print('Registrar conta:')
                print('-'*50)
                tipo = input('C - Corrente\nP- Poupança\n:').upper()
                if tipo in ['C', 'P']:
                    break
                print('ERRO: Digite uma opção válida.')
                sleep(1)  
            print('='*50)
            
            while True:
                NumeroConta = randint(100000000, 999999999)
                if all(list(NumeroConta != conta.numero for banco in sistema['Bancos'] for conta in banco.listaconta)):
                    break
                input(':')

            senha = set_passwd('Digite a senha: ')
                
            DadosConta = [agencia, NumeroConta, senha,input_float('Informe o saldo da conta:')]
            
            if tipo == 'C':
                conta = ContaCorrente(*DadosConta)
                conta.banco = banco
                conta.dadoscliente = cliente
                cliente.conta.append(conta)
                banco.registrar_conta(cliente, conta)
                return conta
            
            conta = ContaPoupanca(*DadosConta)
            conta.banco = banco
            conta.dadoscliente = cliente
            cliente.conta.append(conta)
            banco.registrar_conta(cliente, conta)
            return conta
        return False
    print('Não foi possível abrir conta, pois não há nenhum banco registrado no sistema')
    input('Next:')


def logar() -> bool | None:
    system('clear')
    if sistema['Bancos']:
            if any(banco.listaclientes for banco in sistema['Bancos']):
                bancolog = seleciona_banco()
                cpf = valida_cpf('Informe seu cpf: ')
                posicoes = []
                if any(list(cpf == cliente._id and (posicoes.append(pos) or True) for pos, cliente in enumerate(bancolog.listaclientes))):
                        global Contalogin, Cliente_Main
                        Cliente_Main = bancolog.listaclientes[posicoes[-1]]
                        banckaccounts = []
                        
                        for pos, conta in enumerate(Cliente_Main.conta):
                            if conta.banco.nome == bancolog.nome:
                                banckaccounts.append(conta)
                        
                        while True:
                            def internavisual(banco, banckaccount):
                                system('clear')
                                print('='*50)
                                print(f'{f"Contas no {banco.nome}":^50}')
                                print('-'*50)
                                for pos, conta in enumerate(banckaccount):
                                    print(f'{pos+1} - Conta Corrente do {conta.banco.nome}, agência n°{conta.agencia}.' if isinstance(conta, ContaCorrente)
                                            else f'{pos+1} - Conta Poupança do {conta.banco.nome}, agência n°{conta.agencia}.')
                                print('-'*50)

                            internavisual(bancolog, banckaccounts)
                            escolhaconta = input_int(1, 'Selecione a conta para logar[-1 para abortar]:',False,  internavisual, bancolog, banckaccounts)[0] - 1
                            if escolhaconta == -2:
                                return False

                            if escolhaconta in range(0, len(banckaccounts)):
                                Contalogin = banckaccounts[escolhaconta]
                                break
                            
                            print('Selecione uma conta válida.')
                            sleep(1)


                        tentativas = 0
                        recovery = False
                        while True:
                            if tentativas >= 5:
                                print('Limite de tentativas excedido')
                                sleep(1.5)
                                set_passwd('Digite a nova senha:')
                                Contalogin.senha = set_passwd('Digite novamente para confirmar:')
                                recovery = True
                                
                            if not recovery:
                                senha = set_passwd('Informe a senha da conta[111111 para abortar]: ', True)

                            if senha == 111111:
                                print('Abortando...')
                                sleep(2)
                                return False
                            
                            if senha == Contalogin.senha or recovery:
                                global logado, Bancologin
                                logado = True
                                Bancologin = bancolog

                                print('Logou na conta com sucesso')
                                input('Next: ')
                                return logado
                            
                            print('Senha incorreta, tente novamente.')
                            sleep(1.4)
                            tentativas += 1

                print('Você não possui conta no banco selecionado.')
                input('Next: ')
                return False
            
            print('Bancos registrados ainda não possuem contas abertas.')
            input('Next: ')
            return False
    
    print('Nenhum banco registrado no sistema')
    input('Next:')


def registrar_banco() -> Banco:
        while True:
            system('clear')
            print('='*50)
            BankName = input('Nome do banco:').capitalize()
            if BankName:
                break
            print('ERRO: Nome de banco não pode ser vazio.')
            sleep(1)

        if all(BankName not in sistema['Bancos'][count].nome for count in range(len(sistema['Bancos']))):
            NumeroAgencias = input_int(1 ,'Quantas Agências o banco tem:')[0]
            
            while True:
                agencias = input_int(NumeroAgencias, f'Agência:')
                if all(len(str(agencia)) == 3 for agencia in agencias):
                    break
                print('ERRO: Todos os números de agência devem ter 3 digitos.')
                sleep(1.7)
                system('clear')
            print('='*50)

            Bank = Banco(BankName, agencias, [], [])
            sistema['Bancos'].append(Bank)
            return Bank
        print('ERRO: Nome do Banco já existe no sistema')
        input('Next: ')





Contalogin: Cliente= None
logado: bool = False
Bancologin: Banco = None
if __name__ == '__main__':
    while True:
        if not logado:
            system('clear')
            print('='*50)
            print(f'{"Sistema Bancário":^50}')
            print('='*50)
            print('Criar - Cria conta bancária')
            print('Logar - Loga em conta bancária')
            print('Registrar - Registra um Banco')
            print('Consultar - Consultar bancos do Sistema')
            print('Sair - Encerra programa')
            print('='*50)
            opt = input(':').capitalize()
            if opt == 'Sair':
                system('clear')
                print('Encerrando...')
                sleep(1)
                break
            cmds = {'Criar': lambda: criar_conta(), 
                    'Logar': lambda: logar(), 
                    'Registrar': lambda: registrar_banco(),
                    'Consultar': lambda: consulta_Banco()}
            if cmds.get(opt) != None:
                cmds.get(opt)()
            else:
                system('clear')
                print('Digitou comando errado')
                sleep(1)

        else:
            system('clear')
            print('='*50)
            print(f'{Bancologin.nome:^50}')
            print('='*50)
            print(f'Saldo: R${Contalogin.saldo:.2f}'.replace('.', ',') + '.')
            print(f'Numero da Conta: {Contalogin.numero}.')
            print('-'*50)
            aux = list(str(count) for count in range(1,7))
            iterator = iter(aux)
            print(f'[{next(iterator)}] - Dados da conta')
            print(f'[{next(iterator)}] - Depositar')
            print(f'[{next(iterator)}] - Sacar')

            if isinstance(Contalogin, ContaCorrente):
                print(f'[{next(iterator)}] - Aumentar Limite')

            print(f'[{next(iterator)}] - Transferir')
            print(f'[{next(iterator)}] - Deslogar')
            
            escolha = input(':')

            iterator = iter(aux)
            comandos = {next(iterator): lambda: dados_conta(Cliente_Main),
                        next(iterator): lambda: Contalogin.depositar(input_float(f'Quantos R$ deseja depositar:')),
                        next(iterator): lambda: Contalogin._sacar(input_float('Quantos R$ deseja sacar:')),
                        next(iterator): lambda: Contalogin.increase_limite() if isinstance(Contalogin, ContaCorrente) else None,
                        next(iterator): lambda: Contalogin.transferir(input_int(1, 'Digite o número da conta de destino: ')[0], input_float('Quantos deseja enviar: '))
                        }
            
            if escolha == '6' and isinstance(Contalogin, ContaCorrente) or escolha == '5' and not isinstance(Contalogin, ContaCorrente):
                logado = False
                print('Deslogando...')
                sleep(1)
                continue
            if comandos.get(escolha) != None:
               system('clear')
               comandos.get(escolha)()
               input('Next: ')
            else:
                print('Selecione uma opção válida')
                sleep(1)