class CaesarCipher:
  def __init__(self):
    self.key = 5
    self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  def cipher(self, word: str):
    new_word = ''

    for letter in word:
      index = self.alphabet.index(letter.upper()) + self.key

      if(index > 25):
        index = 1 + self.key

      new_word += self.alphabet[index]

    return new_word.lower()

  def decipher(self, word):
    new_word = ''

    for letter in word:
      index = self.alphabet.index(letter.upper()) - self.key

      if(index < 0):
        index = self.alphabet.count() + self.key

      new_word += self.alphabet[index]

    return new_word.lower()