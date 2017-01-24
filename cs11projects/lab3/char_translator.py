#char_translator.py
import random

#generates and returns a string with a-z jumbled up
def random_permute_chars():
    letters = []
    for i in range(97, 123):
        letters.append(chr(i))
    random.shuffle(letters)
    return ''.join(l for l in letters)

#CharTranslator class
class CharTranslator:

    #init method
    #string should be a random permutation of a-z
    def __init__(self, string):
        #check if string is valid permutation
        
        #instance variable for string permutation
        self.jumbledString = string

    #translate a character
    def translate_char(self, char):
        #which index in the alphabet does the
        #passed char belong to?
        char = char.lower()
        if ord(char) >= 97 and ord(char) <= 122:
            #take that index and find what letter
            #is there in the string permutation
            index = ord(char) - 97
            newChar = self.jumbledString[index]
            return newChar
        return char
    
    #undo translation
    def untranslate_char(self, char):
        #find what index the passed char belongs to
        #in the alphabet, and return the letter that
        #is supposed to be there
        char = char.lower()
        if ord(char) >= 97 and ord(char) <= 122:
            #get index of char in the string permutation
            index = self.jumbledString.index(char)
            #then add index to 97 to get corresponding letter
            return chr(97 + index)
        return char

    
