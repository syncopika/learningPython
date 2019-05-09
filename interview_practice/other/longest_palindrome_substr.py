def longestPalindrome(s):

	# easy cases 
	if len(s) <= 1:
		return s 
	
	if len(s) == 2:
		if s[0] == s[1]:
			return s
		else:
			return s[0]
		
   
	# treat each char as a center of a palindrome, and expand from there 
	longestLen = 0
	longestPal = ""
	
	# start at index 1 for the center as a single character
	for i in range(0, len(s) - 1):
		left = i-1
		right = i+1
		length = 1
		pal = ""
		while left >= 0 and right < len(s):
			if s[left] == s[right]:
				length += 2
				pal = s[left:right+1]
			else:
				break
			left -= 1
			right += 1
		
		if length > longestLen:
			longestLen = length
			longestPal = pal
	
		# but also, if the adjacent character is the same, we need to see if those 2 chars 
		# form a center for a palindrome (i.e. like in an even-length palindrome)
		if s[i] == s[i+1]:
			# we might have a center with 2 of the same character
			# note that we definitely have a palindrome of at least size 2 here
			left = i-1 
			right = i+2 
			length = 2 
			pal = s[i:i+2]
			while left >= 0 and right < len(s):
				if s[left] == s[right]:
					pal = s[left:right+1]
					length += 2 
				else:
					break 
				left -= 1
				right += 1

			if length > longestLen:
				longestLen = length
				longestPal = pal
	
	if longestPal == "":
		return s[len(s)-1]
					
	return longestPal
	
	
### testing
print(longestPalindrome("ccd"))
print(longestPalindrome("abb"))
print(longestPalindrome("aabbbbaac"))
