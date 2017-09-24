#find min depth of a binary tree

from classes import BST, TNode
from time import time

#O(n), goes through entire tree, but what if shortest path is close to root?
def minDepthBasic(node):
	#tree is empty
	if node is None:
		return 0

	#Leaf node
	if node.left is None and node.right is None:
		return 1

	#recur right
	if node.left is None:
		return minDepthBasic(node.right) + 1

	#recur left
	if node.right is None:
		return minDepthBasic(node.left) + 1

	return min(minDepthBasic(node.right), minDepthBasic(node.left)) + 1

#Use level order traversal and return depth of first encountered leaf node
def minDepthImproved(node):

	#tree is empty
	if node is None:
		return 0

	#create empty queue fo traversal
	q = []
	q.append({'node': node, 'depth': 1})

	#level order traversal
	while len(q) > 0:
		#remove first item
		item = q.pop(0)
		node = item['node']
		depth = item['depth']

		#if this is the first leaf node return it's depth
		if node.left is None and node.right is None:
			return depth

		#if the left subtree isn't empty, not a leaf, add to queue
		if node.left is not None:
			q.append({'node': node.left, 'depth': depth+1})

		#if right subtree isn't empty, not a leaf, add to queue
		if node.right is not None:
			q.append({'node': node.right, 'depth': depth+1})

myTree = BST()
myTree.insert(TNode(50))
myTree.insert(TNode(15))
myTree.insert(TNode(10))
myTree.insert(TNode(4))
myTree.insert(TNode(12))
myTree.insert(TNode(40))
myTree.insert(TNode(18))
myTree.insert(TNode(24))
myTree.insert(TNode(13))
myTree.insert(TNode(35))
myTree.insert(TNode(31))
myTree.insert(TNode(81))
myTree.insert(TNode(70))
myTree.insert(TNode(55))
myTree.insert(TNode(90))
t0 = time()
print(minDepthBasic(myTree.root))
t1 = time()
print(minDepthImproved(myTree.root))
t2 = time()

print("algorithm improved by: ", (t1-t0)-(t2-t1))


