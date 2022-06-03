import unittest
from src.caesar import CaesarCipher

class CaesarTest(unittest.TestCase):
  def test_cipher(self):
    caesar =  CaesarCipher()
    caesar.set_base_key(1)
    cipher = caesar.execute('a', 'cipher')
    self.assertEqual(cipher, 'b', "Should be cipher a to b")

  def test_decipher(self):
    caesar =  CaesarCipher()
    caesar.set_base_key(1)
    cipher = caesar.execute('b', 'decipher')
    self.assertEqual(cipher, 'a', "Should be decipher b to a")
