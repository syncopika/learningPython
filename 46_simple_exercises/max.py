def max(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num1
    else:
        return num2
        
        
def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num1 == num2 and num2 == num3:
        return num1
    else:
        return num3
