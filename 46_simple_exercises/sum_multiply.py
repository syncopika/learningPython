def sum(array):
    total = 0
    for i in range(0, len(array)):
        total += array[i]
    return total

def multiply(array):
    total = 1
    for i in range(0, len(array)):
        total *= array[i]
    return total
