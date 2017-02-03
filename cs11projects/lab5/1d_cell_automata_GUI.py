#make a tkinter GUI for the 1d cellular automata

#this prevents having to call tkinter methods like a static method
#i.e. Tkinter.function
from tkinter import *
from automaton import *
import math
import sys

#take command line arguments
arraySize = 150
numStates = 3
numNeighbors = 4

count = 0
for arg in sys.argv[1::]:
    if count == 0 and arg:
        arraySize = int(arg)
    elif count == 1 and arg:
        numStates = int(arg)
        if numStates > 5:
            print("states needs to be less than 6")
            sys.exit(1)
    elif count == 2 and arg:
        numNeighbors = int(arg)
    count += 1
blockSize = (800/arraySize)

#define gui object
class TkAutomaton:

    def __init__(self):

        self.done = 0
        
        self.tk = Tk()

        #set up window
        self.tk.wm_geometry("800x600+20+40")
        self.tk.bind("<Return>", self.finish)
        
        #set up canvas
        self.canvas = Canvas(self.tk, width=800, height=800)
        self.canvas.pack()

        #set up an automaton. each instance of this gui has one automaton.
        #give it default values for now
        self.auto = cellular_automaton_1d(arraySize, numStates, numNeighbors)
        #give it a random transition state table
        self.auto.random_initialize()

        #counter to keep track of currRow coordinate
        self.currRow = 0
        #one color for each state (assuming 3 states)
        self.colors = ["#cccddd", "#ab1ddf", "#567aaf", "#dddfff", "bc1def"]

        #show first generation of cells
        for i in range(0, len(self.auto.get_states())):
            state = self.auto.get_states()[i]
            self.canvas.create_rectangle(i*blockSize,
                                         self.currRow,
                                         i*blockSize + blockSize,
                                         self.currRow + blockSize,
                                         fill=self.colors[state],
                                         outline=self.colors[state])                                      
        self.currRow += blockSize
        self.tk.update()

    #still don't know what this one is for...
    def moveSquareUp(self, s):
        self.canvas.move(s, 0, -50)

    def finish(self, e):
        self.done = 1

    """
    update the picture on the canvas. start at row 0 if end is reached.
    """
    def update(self):
        if self.currRow >= 800:
            self.currRow = 0
        
        #put update code here
        self.auto.update()
        for i in range(0, len(self.auto.get_states())):
            state = self.auto.get_states()[i]
            self.canvas.create_rectangle(i*blockSize,
                                         self.currRow,
                                         i*blockSize + blockSize,
                                         self.currRow + blockSize,
                                         fill=self.colors[state],
                                         outline=self.colors[state])                                                      
        self.currRow += blockSize                                                                                                            
        self.tk.update()

#create instance here
gui = TkAutomaton()

while not gui.done:
    gui.update()
    
