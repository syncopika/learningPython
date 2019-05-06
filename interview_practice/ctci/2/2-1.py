# 2.1 - remove duplicates from a linked list that is unsorted

class Node:
	def __init__(self, value):
		self.value = value 
		self.next = None 
	
def print_list(head):
	curr = head
	while curr != None:
		print(curr.value)
		curr = curr.next

def remove_duplicates(head):
	
	if head == None:
		return None
	
	prev = head 
	curr = head 
	s = set()
	s.add(curr.value)
	
	curr = curr.next
	while curr != None:
		if curr.value not in s:
			s.add(curr.value)
			prev.next = curr 
			prev = curr 
		curr = curr.next
		
	# then finally need to set prev.next to None 
	# i.e. a situation where the last node's value 
	# has already been seen - prev.next would still 
	# be pointing to that node (which should be removed)
	prev.next = None 
	
	# no need to return anything
	
	
# what if we can't use a set or something to store already seen values?
# ...gulp
def remove_duplicates2(head):
	curr = head 
	while curr != None:
		curr2 = curr 
		while curr2 != None and curr2.next != None:
			if curr2.next.value == curr.value:
				curr2.next = curr2.next.next 
			else:
				curr2 = curr2.next 
		curr = curr.next
		

n1 = Node(5)
n2 = Node(1)
n3 = Node(5)
n4 = Node(5)
n5 = Node(1)
n6 = Node(2)
n7 = Node(1)
n1.next = n2 
n2.next = n3 
n3.next = n4 
n4.next = n5 
n5.next = n6
n6.next = n7 

# should get 5,1,2 
remove_duplicates(n1)
print_list(n1)