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

    def rotate(self, n=1):
        for i in range(n):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to_letter(self,letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)


""" The following wiring sequences and turnover notches are directly taken from
    wikipedia {https://en.wikipedia.org/wiki/Enigma_rotor_details} pages on "Enigma Motor Details", which The Germans actually used in the war."""

"""I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
"""
"""print(I.forward(0))"""
