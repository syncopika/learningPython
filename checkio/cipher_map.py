#cipher map


def rotate(array):
    newArr = []
    for i in range(0, len(array)):
        newRow = ""
        for j in range(len(array[0])-1, -1, -1):
            newRow += array[j][i]
        newArr.append(newRow)
    return newArr

def recall_password(tuple1, tuple2):
    msg = ""
    for i in range(0, 4):
        if i > 0:
            tuple1 = rotate(tuple1)
        for j in range(0, len(tuple1)):
            for k in range(0, len(tuple1[0])):
                if tuple1[j][k] == 'X':
                    msg += tuple2[j][k]
    return msg


if __name__ == "__main__":
    print(
        recall_password(
            ('X...',
             '..X.',
             'X..X',
             '....'),
            ('itdf',
             'gdce',
             'aton',
             'qrdi'))
        )
    
