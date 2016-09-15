def getLength(string):
    counter = 0
    flag = True
    while flag:
        try:
            check = string[counter]
            counter += 1
        except IndexError:
            check = 'null'
            flag = False
            return counter
    return 0
