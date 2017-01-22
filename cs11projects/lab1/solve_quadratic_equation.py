#!/usr/bin/env python
#solve a quadratic equation

import sys
import math

nums = []
counter = 0

#returns true if a string has a number
def hasNumber(string):
    return any(char.isdigit() for char in string)


for arg in sys.argv:
    
    #ignore first arg (script name)
    if(counter == 0):
        counter += 1
        continue
    
    if(not hasNumber(arg)):
        print("arguments need to be numbers!")
        sys.exit()
    
    '''
        can also try exception handling
        try:
            nums.append(float(arg))
        except ValueError:
            sys.exit()
    '''

    nums.append(float(arg))


#solve the quadratic equation
def solve(a, b, c):

    #check if any solutions might be complex
    if(math.pow(b, 2) - 4*a*c < 0):
        print("there are no real solutions.")
        return  

    numerator1 = (0-b) + math.sqrt(math.pow(b, 2) - 4*a*c)
    numerator2 = (0-b) - math.sqrt(math.pow(b, 2) - 4*a*c)
    denominator = 2*a
    
    #print formula + solutions
    print("Quadratic equation: " + str(a) + "*x^2 + " + str(b) + "*x + " + str(c) + " = 0")
    print("Solution 1: " + str(float(numerator1 / denominator)))
    print("Solution 2: " + str(float(numerator2 / denominator)))

solve(nums[0], nums[1], nums[2])
