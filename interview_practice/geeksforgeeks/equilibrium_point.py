# given an array of n positive numbers, find the index where the sum of the elements to the left
# is equal to the sum of the elements to the right. 

# questions to ask: will there always be an equilibrium point in the input array?
# what about single element arrays? 

# one way is to do a nested for loop 
def equilibrium(arr):
    currTotal = 0
    for i in range(0, len(arr)):
        # currTotal is the left sum of this current index 
        rightSum = 0
        for j in range(i+1, len(arr)):
            rightSum += arr[j]
        if rightSum == currTotal:
            return i
        currTotal += arr[i]
    return -1

# a better way can be solved in linear time 
def better_equilibrium(arr):
    # first get the total
    currTotal = sum(arr)

    # then traverse the list. the right sum of the current index 
    # can be known by subtracting the current index's value from the total 
    # the left sum is known as we add up by traversing 
    leftSum = 0
    rightSum = currTotal
    for i in range(0, len(arr)):
        rightSum = rightSum - arr[i]
        if leftSum == rightSum:
            return i
        leftSum += arr[i]
    return -1 
                

print(equilibrium([1,3,5,2,2]))
print(better_equilibrium([1,3,5,2,2]))