from caesar import CaesarCipher
from colors import HEADER, CYAN, SUCCESS, FAIL
class Cayce:
  def __init__(self): 
    self.option = None
    self.options = {
      1: { 'key': 'cipher', 'value': 'cifrar' }, 
      2: { 'key': 'decipher', 'value': 'decifrar' }, 
      0: { 'key': 'close', 'value': 'sair' }, 
    }
    self.action = None
    self.caesar = CaesarCipher()

  def get_action(self):
    self.action = self.options[self.option]['key']

  def get_option(self):
    print(f'{CYAN}O que deseja fazer?')
    for option in self.options:
      value = self.options[option]['value']
      print(f'{option} - {value}')

    option_str = input('Escolha uma opção: ')

    if(option_str.isdigit() and int(option_str) in self.options):
      self.option = int(option_str)
    else:
      print(f'{FAIL}Opção errada, tente novamente!\n')

  def get_word(self):
    action_value = self.options[self.option]['value']
    print(f'\nBora {action_value}!')
    return str(input('Digite uma palavra: '))

  def run(self):
    print(f'{HEADER}Cayce Cipher')
    print(f'{HEADER}Programa de Cifra de César\n')

    while self.option  != 0:
      self.option = None
      self.action = None

      while not self.option in self.options:
        self.get_option()

      self.get_action()

      if self.option != 0:
        word = self.get_word()

        new_word = self.caesar.execute(word, self.action)

        print(f'\n{SUCCESS}Resultado: {new_word}\n')
      else:
        print(f'\n{HEADER}Cayce Cipher by weslen.dev (https://weslen.dev/links)')
