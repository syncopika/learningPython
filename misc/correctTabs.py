'''

Python script to correct a file that has a bunch of tabs in it
It replaces any tab with 4 spaces

One reason to use this is so that if the file being corrected were to be hosted 
on Github, the presentation will be much better

'''

import sys

filename = sys.argv[1]

# take the data first 
with open(filename, 'r') as file:
	data = file.read()

# make some changes to the data
# each tab becomes 4 spaces 
data = data.replace('\t', '    ')

# write it back to the same file 
with open(filename, 'w') as file:
	file.write(data)
	
	
'''

for multiple files, try this 
	
import os 

for file in os.listdir("/"):
	
	if file.endswith(".js"):
		correctFile(file)
	


def correctFile(filename):

	with open(filename, 'r') as file:
		data = file.read()
 
	data = data.replace('\t', '    ')
 
	with open(filename, 'w') as file:
		file.write(data)

'''