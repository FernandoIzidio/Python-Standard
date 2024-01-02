from time import sleep
import hashlib
from os import system
Sistema: list[dict] = []

class User:
    def _cipher(self):
        data = vars(self)
        hashobj = hashlib.sha256()
        hashobj.update(self.passwd.encode('utf-8'))
        passwd = hashobj.hexdigest()
        data['passwd'] = passwd
        return data

    def _registrar(self):
        while True:
            system('clear')
            self.username = input('Informe o nome de usuário: ')
            if len(self.username) >= 4:
                break
            input('Nome de usuário deve ter pelo menos 4 digitos\nNext:')
        if all(self.username !=  dados['username'] for dados in Sistema):
            while True:
                system('clear')
                self.passwd = input('Informe a senha de usuario:')
                if len(self.passwd) >= 4:
                    break
                input('ERRO: Deve ter no minimo 4 digitos\nNext:')

            data = self._cipher()  
            Sistema.append(data)
            return data
        
        print('Nome de usuário já esta em uso.')
        sleep(1.8)
        
    def _login(self, attempts):
        system('clear')
        if attempts < 5:
            global user_input
            user_input = input("Informe o nome de usuário:")
            try:
                userlogin = [user_input for dados in Sistema if user_input == dados['username']][0]
            except IndexError:
                userlogin = False
                
            if userlogin:
                self.username = user_input
                self.passwd = input("Informe a senha: ")
                data: dict = self._cipher()

                if data in Sistema:
                    global current_user, logado
                    print('Logou no sistema com sucesso.')
                    sleep(1.5)
                    current_user = self
                    logado = True
                    return 
                else:
                    print('Erro: Usuário ou senha invalida')
                    sleep(1.5)

                return self._login(attempts+1)
            else:
                print('ERRO: Usuário não existe no sistema')
                sleep(1.5)
        else:
            while True:
                system('clear')
                opt = input('Deseja alterar a senha[S/N]: ').upper()
                if opt in ('S', 'N'):
                    break
            if opt == 'S':
                system('clear')
                userposition = []

                if any(user_input == datauser['username'] and (userposition.append(pos) or True) for pos, datauser in enumerate(Sistema)):
                    user_data: dict = Sistema[userposition[-1]]
                    user_data['passwd'] = input('Informe a nova senha: ')

                    self.username = user_data['username']
                    while True:
                        system('clear')
                        self.passwd = user_data['passwd']
                        if len(self.passwd) >= 4:
                            break
                        input('ERRO: Deve ter no minimo 4 digitos\nNext:')

                    user_data = self._cipher()
                    Sistema[userposition[-1]] = user_data
                    print('Senha alterada com sucesso')
                    sleep(1.6)
                else:
                    print('Usuário não existe no sistema')
                    sleep(1.5)
            else:
                print('Tente novamente mais tarde.')
                sleep(1.6)

    def _deslog(self):
        global logado
        logado = False


def consultar_dados():
    for chave, valor in vars(current_user).items():
        print(f'{chave}: {valor}' if chave != 'passwd' else f'{chave}: {"*"*len(valor)}') 
    sleep(2)

current_user: User = None
logado = False
while True:    
    if not logado:
        comandos = {'1': lambda: not system('clear') and User()._registrar(),
                    '2': lambda: User()._login(0) if Sistema else not print('Sistema não possui registros') and sleep(1.5)}
        
        system('clear')
        print('='*50)
        print('[1] - Registrar conta')
        print('[2] - Logar')
        print('[3] - Sair' )
        print('='*50)

        cmduser = input(':')

        if cmduser == '3':
            system('clear')
            print('Encerrando...')
            break

        if comandos.get(cmduser):
            comandos.get(cmduser)()
    else:
        comandos = {'1': lambda: consultar_dados(),
        '2': lambda: current_user._deslog()}
        system('clear')
        print('='*50)
        print('[1] - Consultar dados')
        print('[2] - Deslogar')
        print('='*50)
        cmduser = input(':')

        if comandos.get(cmduser):
            comandos.get(cmduser)()
