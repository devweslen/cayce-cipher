class CaesarCipher:
  def __init__(self):
    self.key = 25
    self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  def execute(self, word: str, command: str):
    new_word = ''

    for letter in word:
      base_index = self.alphabet.index(letter.upper())
      key = self.key

      if command == 'decipher': 
        key *= -1
      
      new_index = base_index + key

      if(new_index > len(self.alphabet) - 1):
        new_index -= len(self.alphabet)
      elif(new_index < 0):
        new_index += len(self.alphabet)

      new_word += self.alphabet[new_index]

    return new_word.lower()