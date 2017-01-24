#!/usr/bin/env python

import sys

#get arguments

counter = 0
args = []
counts = []

for arg in sys.argv:
    if counter == 0:
        counter += 1
        continue
    args.append(arg)

#check if there were no arguments
if counter == 0:
    print('there were no arguments!')
    sys.exit()

#otherwise, go through args array and count the lines in each 
for i in range(0, len(args)):
    lineCounter = 0
    with open(args[i], 'r') as f:
        for line in f:
            lineCounter += 1
    counts.append(lineCounter)

#then print out the line count for each file
for j in range(0, len(args)):
    print(args[j] + " has " + str(counts[j]) + " lines.")
 
