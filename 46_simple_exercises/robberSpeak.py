def isVowel(char):
    if len(char) != 1:
        return "length needs to be 1"
    else:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(0, len(vowels)):
            if vowels[i] == char:
                return True
    return False

def robberSpeak(string):
    newStr = ""
    for i in range(0, len(string)):
        if(not isVowel(string[i]) and string[i] != " "):
            newStr += string[i] + 'o' + string[i]
        else:
            newStr += string[i]
    return newStr
