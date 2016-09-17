def histogram(list):
    for i in range(0, len(list)):
        newStr = ""
        for j in range(0, list[i]):
            newStr += "*"
        print(newStr)
