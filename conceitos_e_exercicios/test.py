from os import system
from time import sleep
from random import choice

dicionario = ['Tartaruga', 'Cachorro', 'Peixe', 'Gato', 'Leao', 'Jacare', 'Tijolo', "Chocolate", "Milho", "Pipoca", "Açucar", "Leite", "Biscoito", "Trigo"]
mistakes = 0
 
escolha = choice(dicionario)
palavra = []
check = []

def iniciar():
    for letra in escolha:
        palavra.append(letra.upper())
        check.append('_')

def encontrar_posicoes(string, caractere):
    posicoes = []
    for pos, letra in enumerate(string):
       if letra == caractere:
          posicoes.append(pos)  
    return posicoes

def mostrar_velha(erros):
    match erros:
        case 0:
            print("  --------")
            print(" /       |")
            print(" |       ")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("-------------", end='')
        case 1:
            print("  --------")
            print(" /       |")
            print(" |       O")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("-------------", end='')
        case 2:
            print("  --------")
            print(" /       |")
            print(" |       O")
            print(" |       |")
            print(" |")
            print(" |")
            print(" |")
            print("-------------", end='')
        case 3:
            print("  --------")
            print(" /       |")
            print(" |       O")
            print(" |      /|")
            print(" |      ")
            print(" |")
            print(" |")
            print("-------------", end='')
        case 4:
            print("  --------")
            print(" /       |")
            print(" |       O")
            print(" |      /|\\")
            print(" |      ")
            print(" |")
            print(" |")
            print("-------------", end='')
        case 5:
            print("  --------")
            print(" /       |")
            print(" |       O")
            print(" |      /|\\")
            print(" |      / ")
            print(" |")
            print(" |")
            print("-------------", end='')
        case _:
            print("  --------")
            print(" /       |")
            print(" |       O")
            print(" |      /|\\")
            print(" |      / \\")
            print(" |")
            print(" |")
            print("-------------", end='')

iniciar()
while True:
  while True:
    system('cls')
    mostrar_velha(mistakes)
    print(f'{" ":>10}', end='')
    print(*check, sep=' ')
    print('')
    print('='*50)
    esc = input('Digite uma letra: ').upper()
    print('='*50)
    if len(esc) == 1:
      break
    system('cls')
    print('='*50)
    print('ERRO: Digite apenas uma letra.')
    print('='*50)
    sleep(2)
    system('cls')

  if esc in palavra:
    temp = encontrar_posicoes(palavra, esc)   
    for position in temp:
       check.pop(position)
       check.insert(position, esc)
  else:
    mistakes += 1

  if '_' not in check:
      system('cls')
      print('='*50)
      print('PARABÉNS VOCÊ VENCEU O JOGO!!!!')
      print('='*50)

      mistakes = 0  
      palavra.clear()
      check.clear()
      escolha = choice(dicionario)
      iniciar()

      while True:
        opt = input('Deseja jogar novamente[S/N]:').upper()
        if opt in ('S', 'N'):
          break
        system('cls')
        print('='*50)
        print('ERRO: Selecione uma opção válida.')
        print('='*50)
        sleep(2)
        system('cls')

      if opt == 'N':
        break

  elif mistakes == 6:
      system('cls')
      print('='*50)
      print('VOCÊ PERDEU!!!')
      print(f'A palavra era: {escolha}')
      print('='*50)

      mistakes = 0  
      palavra.clear()
      check.clear()
      escolha = choice(dicionario)
      iniciar()

      while True:
        opt = input('Deseja jogar novamente[S/N]:').upper()
        if opt in ('S', 'N'):
          break
        system('cls')
        print('='*50)
        print('ERRO: Selecione uma opção válida.')
        print('='*50)
        sleep(2)
        system('cls')

      if opt == 'N':
        break
