from os import system
from time import sleep


def sleep_seconds(seconds):
    def decorator(obj):
        def metodo(self, *args, **kwargs):
            system('cls')
            obj(self, *args, **kwargs)
            sleep(seconds)
        return metodo
    return decorator
    

#Decorator para suprimir e logar erros de funções
def ignore_error(obj): 
    def internal(self, *args, **kwargs):
        try:
            obj(self, *args, **kwargs)
        except ValueError:
            print("Tarefa não encontrada" if self.base_list else "Lista vazia")
    return internal 
class TaskList:
    standardlist = None #Atributo vai dar acesso a única instância

    def __new__(cls, base_list = None) -> 'TaskList':
        if TaskList.standardlist is None:
            cls.standardlist = super().__new__(cls)
            cls.standardlist.base_list = base_list or []
            cls.standardlist.trash = []
        return cls.standardlist 

    @sleep_seconds(1.1)
    def view_list(self):
        if self.base_list:
            print("Lista de tarefas: ", end='\n\t')
            print(*self.base_list, sep='\n\t')
            return
        print("Lista vazia")
    

    @sleep_seconds(0.4)
    @ignore_error
    def remove_task(self, task):
        pos_task = self.base_list.index(task)
        self.trash.append(self.base_list[pos_task])
        self.base_list.pop(pos_task)
    
    @sleep_seconds(0.4)
    @ignore_error
    def unremove_task(self):
        self.base_list.append(self.trash[-1])
        self.trash.remove(self.trash[-1])
    
    @sleep_seconds(0.4)
    @ignore_error
    def amend_task(self, oldvalue, newvalue):
        self.base_list[self.base_list.index(oldvalue)] = newvalue


    def append_task(self, task):
        self.base_list.append(task)

    def __repr__(self) -> str:
        return f"[{', '.join(self.base_list)}]"
    


standard_list = TaskList()

standard_list.append_task("Truco")

standard_list2 = TaskList(["Lista que não entra"])
standard_list2.append_task("Apontam para a mesma referência")
print(TaskList.standardlist)

system("cls")
sleep(1)
TaskList.standardlist.base_list.clear()
t1 = TaskList()

cmds = {
    "1": lambda: t1.view_list(),
    "2": lambda task = lambda: (system('cls') or True) and input("Digite um valor:"): t1.append_task(task()),
    "3": lambda task = lambda: (system('cls') or t1.view_list() or True)  and input("Digite um valor:"): t1.remove_task(task()),
    "4": lambda: t1.unremove_task(),
    "5": lambda old = lambda: ((system('cls') or t1.view_list() or True) and input("Informe o valor antigo:")), new=lambda: (system('cls') or True) and input("Informe o valor novo:"): t1.amend_task(old(), new()),
}
while True:
    print("="*50)
    print(f"{'Lista de Tarefas':^50}")
    print("="*50)
    print('  1 - Visualizar lista')
    print('  2 - Adicionar tarefa')
    print('  3 - Remover Tarefa')
    print('  4 - Refazer Tarefa')
    print("  5 - Corrigir Tarefa")
    print("="*50)

    cmd_choice = input("Digite um comando: ")

    choiced = cmds.get(cmd_choice, None)
    if choiced:
        choiced()
        continue

    print("Comando invalido")
    sleep(0.6)