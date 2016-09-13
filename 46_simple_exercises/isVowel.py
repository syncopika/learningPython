def isVowel(char):
    if len(char) != 1:
        return "length needs to be 1"
    else:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(0, len(vowels)):
            if vowels[i] == char:
                return True
    return False
