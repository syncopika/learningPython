def verify_anagrams(first_word, second_word):
    
    first = list(first_word.lower().replace(" ", ""))
    first.sort()
    
    second = list(second_word.lower().replace(" ", ""))
    second.sort()
    print(first)
    print(second)
    for i in range(0, len(first)):
        if i == len(first) or i == len(second):
            return False
        if first[i] != second[i]:
            return False

    return True
