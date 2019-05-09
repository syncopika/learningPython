# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/

"""
	ideas:
	
	similarly to finding the longest substring with no repeating characters,
	I think we want to traverse the string and keep track of how many distinct characters we've seen so far. 
	
	the hard part I think is knowing where/how to reset the start pointer so we get the correct length.
	
	things we need to track:
	start -> the index of the substring we're currently tracking 
	maxLength
	the number of distinct characters we've seen so far (use a set?)
	something to record the index of each distinct character
	something to record the number of times each distinct character has been seen so far -> this will help us in resetting the start pointer 
	
	questions:
	what if k is greater the number of distinct characters?

	the below is not correct. just keeping it here so I can remember what I thought of. 
	the chuk of code where I check if index - firstSeenIndex[ch] + 1 != timesSeen[ch] does nothold well for any value of k.
	i.e. it may work if k = 2, but not k = 3. :/

	def longest_substr_k_distinct(string, k):

		firstSeenIndex = {}
		timesSeen = {}
		start = 0
		maxLength = 0
		window = []
		
		for index,ch in enumerate(string):
				
			if ch not in firstSeenIndex:
				firstSeenIndex[ch] = index 
				timesSeen[ch] = 1
			else:
				timesSeen[ch] += 1
				# see if the number of times this char has been seen + the index it was last seen at equals this current index 
				# in other words, we want to know if this current char is part of a consecutive chain of the same char. 
				# if it is, we don't update the index. so if we have "aabeeeeeeee", when we look up the index for 'e', we 
				# want to see the index be 3. but if it was like "aabeeeefefefe", we want the index for 'e' to be updated each non-consecutive time its seen 
				if index - firstSeenIndex[ch] + 1 != timesSeen[ch]:
					firstSeenIndex[ch] = index 
					# reset timesSeen 
					timesSeen[ch] = 1
			
			if ch not in window:
				if len(window) == k:
					# if we see a new distinct char that would put the number of distinct chars in the current substring over k
					# sliding window? check the length we have so far, remove the first element, reset start
					if index - start > maxLength:
						maxLength = index - start 
						print(string[start:index+1])
					
					window.pop(0) # so the 2nd distinct element that was seen in the substring now moves to the start of the window 
					window.append(ch)
					start = max(start, firstSeenIndex[window[0]]) # we reset start to be where the 2nd distinct element was first seen 
				else:
					window.append(ch)
			
		# don't forget about if the longest substring is at the end!! 
		if len(string) - start > maxLength:
			return len(string) - start
					
		return maxLength
	
	
	instead, below is the solution that shows up in many places. it's actually pretty straightforward!
	the idea is to keep track of the distinct characters seen so far. by using a map, you can check the 
	number of distinct characters you've seen so far. you also want to use this map to store the number of
	occurrences for each character.
	
	we keep track of the starting index of the substrings we look at. 
	we walk through the string.
	if the size of the map is equal to k, check index-start for the length.
	update the max length accordingly.
	keep adding new chars as you see them until the map's size gets over k. 
	when the map's size is over k, we have to remove a key so that we get the map back down 
	to only having k distinct chars.
	
	remember we were storing number of occurrences for each char in the map? 
	now that we're > k, we need to keep subtracting from keys in the map until one of them 
	gets to 0. then we can remove it from the map and move on to the next substring.
	so, we take our start index and look at the char at that index. 
	subtract 1 from that char's value in the map. 
	check if it's 0 yet.
	if so, remove it from the map. increment the start index! this is how we can move on to 
	the next substring correctly.
	if not yet 0, then we just keep incrementing the start index, subtracting that character's value
	in the map, and checking if we can remove that key.
	
	see: sliding window technique
	
	"""
	
def longest_substr_k_distinct(string, k):

	map = {}
	start = 0
	maxLength = 0
		
	for index,ch in enumerate(string):
		if ch not in map:
			map[ch] = 1
		else:
			map[ch] += 1
			
		while len(map) > k:
			map[string[start]] -= 1
			if map[string[start]] == 0:
				del map[string[start]]
			start += 1
			
		if len(map) == k:
			if index - start + 1 > maxLength:
				maxLength = index - start + 1
		
	return maxLength

# testing 
print(longest_substr_k_distinct("aabbcc", 1)) # 2
print(longest_substr_k_distinct("aabbcc", 2)) # 4
print(longest_substr_k_distinct("aabbcc", 3)) # 6
print(longest_substr_k_distinct("aaabbb", 3)) # 0
print(longest_substr_k_distinct("aaasdfjbsajfnksdjkfhhdhfjksdhkjjkjhghghjzzzzzzzzzzjkllbbb", 3)) # 13
print(longest_substr_k_distinct("aaasdeeeeeeeffffffffff", 3)) # 18
print(longest_substr_k_distinct("aaasdeeeeeeeffffffffff", 2)) # 17 
print(longest_substr_k_distinct("aaasdeeeeeeefffefefefefefefefggggggggggggggggggggggggggg", 3)) # 
print(longest_substr_k_distinct("aaasdeeeeeeefffefefefefefefefggggggggggggggggggggggggggg", 2)) # 28