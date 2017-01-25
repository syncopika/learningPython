#1d cellular automata
import random

class cellular_automaton_1d:

    #set transition table to None by default
    def __init__(self, size, states, neighbors, table = None):
        """
             show an automation where
             @size = number of generations
             @states = number of states from 0 - (states-1)
             @neighbors = number of neighbors on each side
             @table = optional argument, which is an array
             that holds the transition state data for one generation
             of cells
        """
        self.size = size 

        #check if states is a valid num (positive int)
        if states < 0 or neighbors < 0:
            raise ValueError
        
        self.numStates = states
        
        #the number of neighbors on EACH side
        self.numNeighbors = neighbors 

        #set up transition table
        if table is None:
            self.generate_random_table()
        elif not isinstance(table, list):
            raise ValueError
        else:
            #probably should check for more things, like
            #if the table length or contents are wrong
            self.transitionTable = table

        #set up cell array
        self.cellArray = []

        
    def generate_random_table(self):
        """
            generate a random transition state table depending on
            the number of neighbors and states
        """
        array = []
        #formula to figure out how big
        #the transition state table should be
        #based on numStates and numNeighbors
        arrLength = (self.numStates-1)*(2*self.numNeighbors+1) + 1
        for i in range(0, arrLength):
            array.append(random.randint(0,self.numStates-1))

        self.transitionTable = array

        
    def random_initialize(self):
        """set up a randomized cell array for the first generation"""
        for i in range(0, self.size):
            self.cellArray.append(random.randint(0, self.numStates-1))

            
    #helper function for finding sum of neighbors and self
    def getSum(self, currIndex):
        """
            get the sum of a particular cell's state and its neighbors' states
            this sum is the index to look for in the transitional table, which
            will show the next state for the particular cell
        """
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
        """update the current cell generation to the next one"""
        #generate the next generation of cells
        tempArr = []
        for i in range(0, len(self.cellArray)):
            tempArr.append(self.transitionTable[self.getSum(i)])
        #then change old array to temp array
        self.cellArray = tempArr
        

    def get_states(self):
        """see the states of the current generation of cells"""
        copy = self.cellArray[:]
        return copy
    

    def printCells(self):
        """
             print out the current generation. if the number of states
             is fewer than 10, print them all out on one line, with no commas
             otherwise, just print the array
        """
        if self.numStates < 10:
             print(''.join(str(num) for num in self.cellArray))
        else:
            print(self.cellArray)
    


#main method
if __name__ == "__main__":

    try:
        a = cellular_automaton_1d(70, 3, 3)
        a.random_initialize()
        a.printCells()

        for i in range(0, 100):
            a.update()
            a.printCells()
            
    except ValueError:
        print("there's something wrong with your arguments!")

