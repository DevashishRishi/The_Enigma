"""
    Reflector: A
    Rotors: I-II-III
    Plugboard: A-R, G-K, O-X (Here only these alphabets are mapped.)
    Message: A => X
"""

import pygame
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

# set pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma Simulator")

# create fonts
MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# global variables
WIDTH=1600
HEIGHT=900
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS={"Top":200,"Bottom":200, "Left":100, "Right":100}
GAP=100
INPUT=""
OUTPUT=""
PATH=[]

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
PB = Plugboard(["AB","CD", "EF"])

# define enigma machine
ENIGMA = Enigma(B, I, II, III, PB, KB)

# set the rings
ENIGMA.set_rings((1,1,1))

# encipher a letter
# print(ENIGMA.encipher("A"))

# set message key
ENIGMA.set_key("CAT")
# ENIGMA.r3.show()

"""# encipher message
message="ONE PIECE IS REAL"
cipher_text=""
for letter in message:
    cipher_text = cipher_text+ENIGMA.encipher(letter)
print(cipher_text)"""

"""I.show()
I.rotate_to_letter("G")
I.show()"""

animating=True
while animating:
    # background
    SCREEN.fill("#333333")

    # text input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH/2, MARGINS["Top"]/3))
    SCREEN.blit(text, text_box)

    # text output
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["Top"] / 3+25))
    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)



    #update screen
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key==pygame.K_SPACE:
                INPUT=INPUT+" "
                OUTPUT=OUTPUT+" "
            else:
                key=event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter=key.upper()
                    INPUT=INPUT+letter
                    PATH, cipher=ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT=OUTPUT+cipher
                    print(INPUT)
