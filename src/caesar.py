class CaesarCipher:
  def __init__(self):
    self.base_key = 25
    self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  def set_base_key(self, key):
    self.base_key = key

  def execute(self, word: str, command: str):
    new_word = ''

    for letter in word:
      base_index = self.alphabet.index(letter.upper())
      key = self.base_key

      if command == 'decipher': 
        key *= -1
      
      new_index = base_index + key

      alphabet_length = len(self.alphabet)

      if(new_index > alphabet_length - 1):
        new_index -= alphabet_length
      elif(new_index < 0):
        new_index += alphabet_length

      new_word += self.alphabet[new_index]

    return new_word.lower()