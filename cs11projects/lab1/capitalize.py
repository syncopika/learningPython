#!/usr/bin/env python

import sys

#capitalize all lines from input file and output them in another

count = 0

#get file
for arg in sys.argv:
    if count == 0:
        count += 1
        continue
    elif count == 1:
        count += 1
        f = arg
    elif count == 2:
        outputName = arg

#if too few or many arguments
if count > 2:
    print('Too many arguments!')
    sys.exit()
elif count == 0:
    print('Not enough arguments!')
    sys.exit()    

file = open(f, 'r')
outputFile = open(outputName, 'w')

for line in file:
    outputFile.write(line.upper())

file.close()
outputFile.close()

print('done!')


