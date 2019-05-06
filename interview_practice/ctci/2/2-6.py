# 2.6 - palindrome: check if a linked list is a palindrome 

class Node:
	def __init__(self, value):
		self.value = value 
		self.next = None 
		
"""

	ideas:
		use an auxiliary data structure like a list to collect all the values and then check that for palindrome?
		use a stack? find list length first. then when you get halfway in a 2nd pass start popping values off the stack to compare 
		
		let's use 2 pointers. initially they both start at the beginning. 
		increment one by one each iteration, and the other by 2 nodes (this way the 2nd ptr is moving twice as fast as the first). at each iteration ptr1's node value will be pushed to the stack.
		when ptr 2 reaches the end of the list (when ptr2 = null), it's time to pop off the stack the last value and compare. the first ptr should be in the middle of the list.   
		
		here are some examples:
		
		here is a linked list of 5 nodes (odd-length)
		O -> O -> O -> O -> O 
				  ^         ^
				  ptr1      ptr2
		
		when ptr2 reaches the end, ptr1 will be in the middle node (make sure you don't add this value to the stack!). 
		we use ptr2 to keep track of the length. we see that it's odd because ptr2 is on the last node. we stope moving ptr2 is it becomes null or its next is null.
		since we're evaluating if the list is a palindrome,
		and we have odd length, we skip the middle node. so move ptr1 to the next node, 
		and then start popping off the stack to compare. 
		
		here is a linked list of 6 nodes (even-length)
		O -> O -> O -> O -> O -> O -> null
		               ^               ^
					  ptr1           ptr2
		
		in the even-length case, we don't have to adjust ptr1 when ptr2 hits the last node. 
		we can start comparing right away. 
		
"""

def palindrome(node):

	if node == None:
		return False 
		
	if node.next == None:
		return True

	stack = []
	
	ptr1 = node 
	ptr2 = node 
	
	while ptr2 and ptr2.next != None:
		stack.append(ptr1.value)
		ptr1 = ptr1.next 
		ptr2 = ptr2.next.next # hop 2 nodes over  
		
	# we can use the value ptr2	to determine parity
	if ptr2 != None:
		# we have an odd length
		ptr1 = ptr1.next 
		
	# pop stack and compare 
	while ptr1 != None:
		last = stack.pop()
		if ptr1.value != last:
			return False 
		ptr1 = ptr1.next
			
	return True 

# testing
n1 = Node(1)
n2 = Node(2)
n1.next = n2 

# 3-4-5-4-3
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(4)
n7 = Node(3)
n3.next = n4 
n4.next = n5 
n5.next = n6 
n6.next = n7 

# 3-1-1-3
n8 = Node(3)
n9 = Node(1)
n10 = Node(1)
n11 = Node(3)
n8.next = n9 
n9.next = n10 
n10.next = n11 

print(palindrome(n1)) # false 
print(palindrome(n3)) # true 
print(palindrome(n8)) # true 

# 3-4-4-1
n3.next = n4 
n4.next = n6 
n6.next = n9 
print(palindrome(n3)) # false 