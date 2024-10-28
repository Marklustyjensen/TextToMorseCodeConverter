#######################################
#                                     #
#  Script created by Mark L. Jensen   #
#  marklustyjensen@gmail.com          #
#  www.marklustyjensen.com            #
#                                     #
#######################################

# First a dictionary is created to translate a regular string into morse code.
Translator = {
    "A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.", "G": "_ _.", "H": "....", "I": "..", "J": "._ _ _", "K": "_._", "L": "._..", "M": "_ _", "N": "_.", "O": "_ _  ", "P": "._ _.", "Q": "_ _._", "R": "._.", "S": "...", "T": "_", "U": ".._", "V": "..._", "W": "._ _", "X": "_.._", "Y": "_._ _", "Z": "_ _..", " ": "/", "0": "_ _ _ _ _", "1": "._ _ _ _", "2": ".._ _ _", "3": "..._ _", "4": "...._", "5": ".....", "6": "_....", "7": "_ _...", "8": "_ _ _..", "9": "_ _ _ _.", ".": "._._._", ",": "_ _.._ _", "?": ".._ _.."
}

# Asking the user for the string to translate.
string = input("Write the sentence you want translated into morse code: ").upper()

# Creating an empty list to add the translated letters to.
Morse = []

# Looping through each letter in the string, translating the letter into morse code.
for i in range(len(string)):
    letter = Translator[string[i]]
    Morse.append(letter)

# Printing the translated string.
print(Morse)
