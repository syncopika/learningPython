# reverse a linked list 

class Node:
	
	def __init__(self, value):
		self.next = None 
		self.val = value 
		
class LinkedList:

	def __init__(self):
		self.head = None 
		
	def add(self, node):
		if self.head == None:
			self.head = node 
		else:
			curr = self.head 
			while curr.next != None:
				curr = curr.next 
			curr.next = node 

	def traverse(self):
		curr = self.head 
		while curr != None:
			print(curr.val)
			curr = curr.next 

			
def reverse(list):
	
	# grab the 2nd node 
	temp = list.head.next

	# point the first node to None (it's a new tail now)
	list.head.next = None 
	
	# then go through rest of list and repoint each node's next 
	curr = temp
	prev = list.head 
	while curr != None:
		nextCurr = curr.next 
		curr.next = prev 
		prev = curr
		curr = nextCurr 
	
	list.head = prev 
			
			
list1 = LinkedList() 
list1.add(Node(4))
list1.add(Node(1))
list1.add(Node(6))
list1.add(Node(2))

list1.traverse()

# reverse list 
reverse(list1)
print("----- after reversal ------")
list1.traverse()