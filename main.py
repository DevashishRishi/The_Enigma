"""
    Reflector: A
    Rotors: I-II-III
    Plugboard: A-R, G-K, O-X (Here only these alphabets are mapped.)
    Message: A => X
"""

from keyborad import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# historical enigma rotors and reflectors
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

"""This also has been taken directly from wikipedia: https://en.wikipedia.org/wiki/Enigma_rotor_details"""
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard
KB = Keyboard()
PB = Plugboard(["AR","GK", "OX"])

# define enigma machine
ENIGMA = Enigma(B, I, II, III, PB, KB)

# encipher a letter
# print(ENIGMA.encipher("A"))

# set message key
ENIGMA.set_key("DOG")
ENIGMA.r3.show()

# encipher message
message="TEST"
cipher_text=""
for letter in message:
    cipher_text = cipher_text+ENIGMA.encipher(letter)
print(cipher_text)

"""I.show()
I.rotate_to_letter("G")
I.show()"""
