import pygame

class Rotor:
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def show(self):
        print(self.left)
        print(self.right)
        print("")

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]


    def rotate_to_letter(self,letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, n):
        # rotate the rotors backward
        self.rotate(n-1, forward=False)

        # adjust the turnover notch in relationship to the wiring
        n_notch="ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch="ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - n)%26]

    def draw(self, screen, x, y, w, h, font):
        #rectangle
        r=pygame.Rect(x,y,w,h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        # letters
        for i in range(26):

            # left hand side
            letter=self.left[i]
            letter=font.render(letter, True, "grey")
            text_box=letter.get_rect(center= (x+w/4, y+(i+1)*h/27))

            # highlight top letter
            if i==0:
                pygame.draw.rect(screen, "teal", text_box, border_radius=5)

            # highlight turnover notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, "white", text_box, border_radius=5)

            screen.blit(letter, text_box)


            # right hand side
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w*3/4, y+(i+1)*h/27))
            screen.blit(letter, text_box)




""" The following wiring sequences and turnover notches are directly taken from
    wikipedia {https://en.wikipedia.org/wiki/Enigma_rotor_details} pages on "Enigma Motor Details", which The Germans actually used in the war."""

"""I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
"""
"""print(I.forward(0))"""
