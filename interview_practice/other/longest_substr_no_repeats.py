# length of longest substring without repeating characters 
# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

"""
	idea:
	a map that keeps track of characters seen and their last index seen 	
	longest string length seen so far 
"""

def longest_substr(string):
	map = {}
	longestLength = 0
	start = 0

	for idx,ch in enumerate(string):
		if ch not in map:
			map[ch] = idx 
		else:
			currLength = idx - start 
			if currLength > longestLength:
				longestLength = currLength 
				print(string[start:idx])
			
			# restart for next substring
			# here we want to figure out where the new substring should start 
			# by taking the maximum of the old starting index and the index we last 
			# saw the current char + 1. we do this because sometimes we don't want 
			# to start the substring too far back since there might be duplicate chars in there.
			start = max(map[ch] + 1, start)
			map[ch] = idx
	
	# the longest substring might be at the very end, so catch those here
	if len(string) - start > longestLength:
		return len(string) - start
			
	return longestLength 
	
# testing 
print(longest_substr("ABDEFGABEF")) # 6
print("-------------")
print(longest_substr("GEEKSFORGEEKS")) # 7
print("-------------")
print(longest_substr("BBBB")) # 1
print("-------------")
print(longest_substr("abcabcbb")) # 3
print("-------------")
print(longest_substr("pwwkew")) # 3
print("-------------")
print(longest_substr("abba")) # 2
print("-------------")
print(longest_substr("abcabcskdfnkjasdfnkjadsbsbb")) # 8 (fnkjadsb)
print("-------------")
print(longest_substr("dvdf")) # 3
print("-------------")
print(longest_substr("abba")) # 2