from os import system
from time import sleep
from random import choice

class Game_Main:
   def __init__(self) -> None:
      self.words =  ['Geladeira', 'Fogao', 'Microondas', 'Forno', 'Lavaloucas', 'Espremedor', 'MaquinadeLavar', 'AspiradordePo', 'Ventilador', 'ArCondicionado', 'Cadeira', 'Sofa', 'Mesa', 'Estante', 'Cama', 'GuardaRoupa', 'Comoda', 'Abajur', 'Luminaria', 'Quadro', 'Piano', 'Violao', 'Flauta', 'Trompete', 'Bateria', 'Saxofone', 'Harpa', 'Gaita', 'Violino', 'Clarinet', 'Caneta', 'Lapis', 'Caderno', 'Borracha', 'Tesoura', 'Regua', 'Pincel', 'Tinta', 'Lousa', 'Apontador']

      self.mistakes = 0
      self.finish = False
      self.secret: Secret_Word = Secret_Word(self)
      self.userinsert: User_Attempt = User_Attempt(self)
      self.gameinterface: Game_Interface = Game_Interface(self)

   def check_game_status(self):
      if '_' not in self.secret.currentword:
        system('clear')
        print('='*50)
        print('PARABÉNS VOCÊ VENCEU O JOGO!!!!')
        print('='*50)
        self.finish = True
      elif self.mistakes == 6:
        system('clear')
        print('='*50)
        print('VOCÊ PERDEU!!!')
        print(f'A palavra era: {self.secret.wordchoiced}')
        print('='*50)
        self.finish = True
   
   
   def init_game(self):
      self.check_game_status()
      if not self.finish:
        self.userinsert.append_attempt_and_check_it()

      

class Secret_Word:
    def __init__(self, object: Game_Main) -> None:
       self.game: Game_Main = object
       self.wordchoiced = choice(self.game.words).upper()
       self.currentword = ['_' for letter in self.wordchoiced]


class User_Attempt:
    def __init__(self, object_main:Game_Main) -> None:
       self.game: Game_Main = object_main

    
    def append_attempt_and_check_it(self):
       while True:
          system('clear')
          self.game.gameinterface.show_interface()
          letter = input('Digite uma letra: ').upper()
          if len(letter) == 1:
             break
          print('Digite apenas uma letra.')
          sleep(1.5)

       if letter in self.game.secret.wordchoiced:
           for pos, secretletter in enumerate(self.game.secret.wordchoiced):
              if letter == secretletter:
                 self.game.secret.currentword.pop(pos)
                 self.game.secret.currentword.insert(pos, letter)
       else:
           self.game.mistakes += 1    
          

class Game_Interface:
   def __init__(self, object: Game_Main) -> None:
      self.game: Game_Main = object
   

   def show_interface(self):
      system('clear')
      match self.game.mistakes:
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
      
      print(f'{"":>10}', end='')
      print(*self.game.secret.currentword, sep=' ')

Game =  Game_Main()
while True:
  Game.init_game()
  if Game.finish:
    while True:
      system('clear')
      Game.check_game_status()
      opt = input('Deseja jogar novamente[S/N]:').upper()
      if opt in ('S', 'N'):
        break
      print('Digite uma opção válida.')
      sleep(1.3)
    
    if opt == 'N':       
        system('clear')
        print('Encerrando...')
        break
    else:
       Game = Game_Main()
