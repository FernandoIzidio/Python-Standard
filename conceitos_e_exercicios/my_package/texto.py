def printbonito(text:str):
    print('='*len(text))
    print(text)
    print('='*len(text))

printbonito(f'Nome do módulo {__name__}')