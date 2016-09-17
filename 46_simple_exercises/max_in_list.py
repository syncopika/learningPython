def max_in_list(list):
    currentLargest = list[0]
    for i in range(1, len(list)):
        if(list[i] > currentLargest):
            currentLargest = list[i]
    return currentLargest
