def overlapping(list1, list2):
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list2[j] == list1[i]:
                return True
    return False
