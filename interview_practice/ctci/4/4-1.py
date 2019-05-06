# 4.1 - route between nodes
# given a directed graph, find out whether there is a route between 2 nodes


"""

	questions:
	- can we assume no cycles? can there be a cycle? 
	
	ideas:
	1. dfs or bfs. since we have a graph already, we just need to do a search from one node to the other.
	   since it's directed, source and target matter. but maybe can clarify: if some route exists either between 
	   node 1 and node 2, should I still return true? if so, then need to check when node1 = source and when node2 = source. 

""" 

# helper function so we can use the same code to check node1 to node2 and node2 to node1
def has_route_helper(graph, node1, node2):
	stack = [node1]
	
	while len(stack) != 0:
		curr = stack.pop()
		for neighbor in graph[curr]:
			if neighbor == node2:
				return True
			stack.append(neighbor)
	
	return False 

def has_route(graph, node1, node2):
	# assuming graph is represented as an adjacency list
	return has_route_helper(graph, node1, node2)
	
"""
    7
    ^
    |
	1 -> 3 -> 8    
	     |     
		 V   
		 5 -> 6 -> 2
                

"""
	
graph = {1:[3,7],3:[8,5],7:[],8:[],5:[6],6:[2], 2:[]}

print(has_route(graph, 1, 8)) # true 
print(has_route(graph, 3, 2)) # true 
print(has_route(graph, 8, 1)) # false 
print(has_route(graph, 6, 5)) # false
print(has_route(graph, 2, 8)) # false
print(has_route(graph, 7, 8)) # false
