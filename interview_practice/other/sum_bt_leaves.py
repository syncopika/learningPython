# count leaves in a binary tree 

class TreeNode:
	def __init__(self, value):
		self.left = None 
		self.right = None
		self.value = value 
		
	def addLeft(self, node):
		self.left = node 
		
	def addRight(self, node):
		self.right = node 


def sumLeaves(root):
	return sumLeavesHelper(root)
	
def sumLeavesHelper(root):
	# base cases
	if root == None:
		return 0
	if root.left == None and root.right == None:
		return root.value  
	else:
		return sumLeavesHelper(root.left) + sumLeavesHelper(root.right)
		
		
tree = TreeNode(2)
node1 = TreeNode(4)
node2 = TreeNode(5)

# leaf nodes that will be part of the sum
leaf1 = TreeNode(0)
leaf2 = TreeNode(1)
leaf3 = TreeNode(3)

tree.addLeft(node1)
tree.addRight(node2)
node1.addLeft(leaf1)
node1.addRight(leaf2)
node2.addRight(leaf3)

print(sumLeaves(tree))