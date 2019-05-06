# return Kth to last element of a singly linked list

class Node:
	def __init__(self, value):
		self.value = value 
		self.next = None 

"""
	some ideas:
	
	option 1:
	1. one pass to find out how many nodes 
	2. second pass to get to (n-k)th node 

	OR 
	
	option2 :
	we can just do one pass! 
	have 2 pointers, one that starts at the first node, and another that starts on the node that is k nodes away from the first node. 
	then increment each one by one node until the 2nd pointer hits null. at that point the first pointer should be at the answer. 
	
	questions to ask!!! 
	1. can we be sure there will always be a kth to last node?
	   for example, what if we get a linked list of size 2 but we're 
	   asked to find the 5th to last node or something like that? I guess 
	   I'm asking can we be sure k will always be less than n, where n = number of nodes? 
	2. what if k = 0? I'm guessing return null since if k = 1 I should return the last node?

	I'm going to make the following assumptions:
		- k may not be less than n 
		- k = 0 should return null 
		
	pseudocode for option 2:
	
		if k == 0:
			return null
	
		ptr1 = head 
		ptr2 = head
		count = 0
		
		// start ptr2 k nodes away
		while ptr2 != null and count < k:
			ptr2 = ptr2.next
			count++
			
		// check if count is k. this is one way to check if ptr2 is really k nodes ahead of ptr1 
		if count != k:
			return null
		
		while ptr1 != null and ptr2 != null:
			ptr1 = ptr1.next
			ptr2 = ptr2.next
		
		return ptr1 
"""

def kth_to_last(node, k):
	if k == 0:
		return None 
	
	ptr1 = node
	ptr2 = node 
	
	# move ptr2 k nodes away from ptr1 
	count = 0 
	while ptr2 != None and count < k:
		count += 1
		ptr2 = ptr2.next 
	
	# make sure it is possible to have a difference of k nodes 
	if count != k:
		return None
	
	while ptr1 != None and ptr2 != None:
		ptr1 = ptr1.next 
		ptr2 = ptr2.next
		
	return ptr1 
	
	
# testing 
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.next = n2 
n2.next = n3 
n3.next = n4 
n4.next = n5 
n5.next = n6
n6.next = n7 

print(kth_to_last(n1, 0)) # should be None
print(kth_to_last(n1, 9)) # should be None
print(kth_to_last(n1, 1).value) # should be 7
print(kth_to_last(n1, 2).value) # should be 6
print(kth_to_last(n1, 7).value) # should be 1