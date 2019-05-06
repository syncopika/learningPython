# 2.3 - delete middle node 
# given only access to a node in the middle of a linked list, delete that node 

class Node:
	def __init__(self, value):
		self.value = value 
		self.next = None 
		
def print_list(head):
	curr = head
	while curr != None:
		print(curr.value)
		curr = curr.next

"""

	questions!
	the question specifically says the 'middle' of the linked list, so we don't have to 
	worry about the given node being the last node in the list. 
	
	can we be passed null?

	idea:
	take the information from the next node and put it in the current node.
	then make sure you reconnect the next pointer to next.next so we skip the node 
	we took info from.

"""

def delete_middle_node(node):

	if node == None:
		return 
	
	nextNode = node.next 
	node.value = nextNode.value 
	node.next = nextNode.next
	
	
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

delete_middle_node(n4)
print_list(n1)