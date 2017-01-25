#1d cellular automata
#http://stackoverflow.com/questions/4841782/python-constructor-and-default-value
import random

class cellular_automaton_1d:

    def __init__(self, size, states, neighbors, table):
        self.size = size
        self.numStates = states # range: 0 - (states-1)
        self.numNeighbors = neighbors #the number of neighbors on EACH side
        self.transitionTable = table
        self.cellArray = []

    def generate_random_table(self):
        array = []
        #formula to figure out how big
        #the transition state table should be
        #based on numStates and numNeighbors
        arrLength = (self.numStates-1)*(2*self.numNeighbors+1) + 1
        for i in range(0, arrLength):
            array.append(random.randint(0,self.numStates-1))

        self.transitionTable = array

    def random_initialize(self):
        for i in range(0, self.size):
            self.cellArray.append(random.randint(0, self.numStates-1))

    #helper function for finding sum of neighbors and self
    #the sum = the index in transition table => which holds next state
    def getSum(self, currIndex):
        #handle cases where left neighbors or right neighbors would
        #be out of bounds
        leftBound = currIndex - self.numNeighbors
        rightBound = currIndex + self.numNeighbors
        if leftBound <= 0:
            total = self.cellArray[currIndex]
            #add the indices that are within the array's range
            total += sum(self.cellArray[0:currIndex])
            #then calculate right neighbors
            total += sum(self.cellArray[currIndex+1:rightBound+1])
            return total
        elif rightBound >= len(self.cellArray):
            total = sum(self.cellArray[currIndex:len(self.cellArray)])
            total += sum(self.cellArray[currIndex-self.numNeighbors:currIndex])
            return total
        else:
            total = self.cellArray[currIndex]
            total += sum(self.cellArray[currIndex-self.numNeighbors:currIndex])
            total += sum(self.cellArray[currIndex+1:self.numNeighbors+currIndex+1])
            return total
                    
    
    def update(self):
        #generate the next generation of cells
        tempArr = []
        for i in range(0, len(self.cellArray)):
            tempArr.append(self.transitionTable[self.getSum(i)])
        #then change old array to temp array
        self.cellArray = tempArr

    def get_states(self):
        copy = self.cellArray[:]
        return copy

    def printCells(self):
        if self.numStates < 10:
             print(''.join(str(num) for num in self.cellArray))
        else:
            print(self.cellArray)
    


#main method
if __name__ == "__main__":
    a = cellular_automaton_1d(70, 2, 1, [0, 1, 1, 0])
    a.random_initialize()
    a.printCells()

    for i in range(0, 100):
        a.update()
        a.printCells()

