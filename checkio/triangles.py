#angles of triangle
import math

def isTriangle(len1, len2, len3):
    if not len1 + len2 > len3:
        return False
    elif not len2 + len3 > len1:
        return False
    elif not len1 + len3 > len2:
        return False
    return True

def angles(len1, len2, len3):

    if len1 == len2 and len1 == len3:
        return [60, 60, 60]

    if isTriangle(len1, len2, len3):
        angles = []
        angC = math.acos((len1**2 + len2**2 - len3**2) / (2*len1*len2))*(180/math.pi)
        angB = math.acos((len1**2 + len3**2 - len2**2) / (2*len1*len3))*(180/math.pi)
        angA = round(180 - angC - angB)

        angles.append(round(angC))
        angles.append(round(angB))
        angles.append(angA)
        angles.sort()
        return angles
        
    return [0, 0, 0]



if __name__ == "__main__":
    a = 5
    b = 4
    c = 3
    print(angles(a,b,c))
