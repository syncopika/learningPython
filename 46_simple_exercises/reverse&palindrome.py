def reverse(string):
    newStr = ""
    for i in range(len(string)-1, -1, -1):
        newStr += string[i]
    return newStr

def is_palindrome(string):
    if string == reverse(string):
        return True
    return False
