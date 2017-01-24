#tower of hanoi - recursive problem
import sys

# get the num of disks as argument
for arg in sys.argv[1::]:
    n = int(arg)

#start class Hanoi
class Hanoi:
    
    #constructor function
    def __init__(self, disks):
        #set up pegs
        self.peg1 = range(disks, 0, -1)
        self.peg2 = []
        self.peg3 = []     
        self.numDisks = disks

    #display the disks for each peg
    def display_pegs(self):
        print("0: " + self.arrayToString(self.peg1))
        print("1: " + self.arrayToString(self.peg2))
        print("2: " + self.arrayToString(self.peg3))
        print("--------------------")

    #convert array to string
    def arrayToString(self, array):
        s = " "        
        for i in range(0,len(array)):
            s += str(array[i]) + " "
        return s
            
    #move function, for moving a disk from a peg to another  
    def move(self, source, destination):
        if(not destination or source[-1] < destination[-1]):
            disk = source.pop()
            destination.append(disk)
    
    #solve helper function
    def solve_helper(self, peg1, peg2, peg3, num):
  
        #base case
        if num == 1:
            #just move the disk from peg1 to peg2
            self.move(peg1, peg2)            
            return
        
        #recursion
        self.solve_helper(peg1, peg3, peg2, num-1)
        
        #display pegs
        self.display_pegs()

        self.move(peg1, peg2)

        #display pegs
        self.display_pegs()

        self.solve_helper(peg3, peg2, peg1, num-1)   


    #solve function
    def solve(self):
        self.display_pegs()
        self.solve_helper(self.peg1, self.peg2, self.peg3, self.numDisks)
        self.display_pegs()

# end of Hanoi class

#solve the problem
h = Hanoi(n)
h.solve()

