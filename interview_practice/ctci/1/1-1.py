#1.1 is unique - determine if a string has all unique characters

"""

	ideas:
		- use a set to keep track of characters seen already 
		- what if we can't use any data structures?
			- can use a nested for loop 
		- maybe if the string is mutable, like in C (not string literals though), we can sort? 

"""

def is_unique(string):
	s = set()
	for ch in string:
		if ch in s:
			return False 
		s.add(ch)
		
	return True
	

def is_unique2(string):

	for i in range(0, len(string)):
		for j in range(i + 1, len(string)):
			if string[i] == string[j]:
				return False 
	return True 
	
	
# testing 
s1 = "hello"
s2 = "abcdefgh"

print(is_unique(s1)) # false
print(is_unique2(s1)) # false 

print(is_unique(s2)) # true
print(is_unique2(s2)) # true 
