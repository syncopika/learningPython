from functools import reduce
from math import floor

def int_to_bin(num):

    binary = ""

    rest = num

    while rest > 0:
        rem = rest % 2
        binary += str(rem)
        rest = floor(rest/2)
    
	# returns the sum of all the 1's in the binary number 
    count = reduce(lambda x,y: x+1 if int(y) == 1 else x, list(binary[::-1]), 0)

    return count


if __name__ == "__main__":

    print(int_to_bin(5))
    print(int_to_bin(12))
