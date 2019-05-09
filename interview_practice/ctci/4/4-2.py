# 4.2 minimal tree 
# create a BST with minimal height given an array of sorted, unique integers 
# note that height = number edges from root to leaf 

class TreeNode:

	def __init__(self, val):
		self.value = val 
		self.left = None 
		self.right = None 
		
	def get_height(self):
		return self.get_height_helper(self, 0)
		
	def get_height_helper(self, node, count):
		if node == None:
			return count - 1
		return max(self.get_height_helper(node.left, count + 1), self.get_height_helper(node.right, count + 1))

"""

	ideas: 
		use recursion.
		start at the middle of the array, which will be the root. 
		then recurse on left and right halves. 



"""

def minimal_tree(arr):

	if len(arr) == 1:
		return TreeNode(arr[0])
	
	mid = len(arr)//2
	newNode = TreeNode(arr[mid])
	
	newNode.left = minimal_tree(arr[0:mid])
	
	if mid+1 >= len(arr):
		newNode.right = None 
	else:
		newNode.right = minimal_tree(arr[mid+1:len(arr)])
	
	return newNode
	
# testing 
n1 = TreeNode(1)
#print(n1.get_height())

n2 = TreeNode(2)
n1.right = n2 
#print(n1.get_height())

arr = [1,2,3,4,5,6]
tree = minimal_tree(arr)
#print(tree.value)
#print(tree.left.value)
#print(tree.left.left.value)
#print(tree.left.right.value)
#print(tree.right.value)
#print(tree.right.left.value)
#print(tree.right.right)
print(tree.get_height()) # 2 


arr = [1,2,3]
tree = minimal_tree(arr)
print(tree.get_height()) # 1



	
