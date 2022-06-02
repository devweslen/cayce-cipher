from caesar import CaesarCipher

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
    print('O que deseja fazer?')
    for option in self.options:
      value = self.options[option]['value']
      print(f'{option} - {value}')

    self.option = int(input('Escolha uma opção: '))

  def get_word(self):
    return str(input('Digite uma palavra: '))

  def run(self):
    print('Cayce Cipher')
    print('Programa de Cifra de César\n')

    while self.option  != 0:
      self.option = None
      self.action = None

      while not self.option in self.options:
        self.get_option()

      self.get_action()

      if self.option != 0:
        word = self.get_word()

        new_word = self.caesar.execute(word, self.action)

        print(f'\n\nResultado: {new_word}\n\n')
      else:
        print('\nCayce Cipher by weslen.dev (https://weslen.dev/links)')
