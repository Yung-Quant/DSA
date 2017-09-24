#search BST

from classes import TNode, BST

#driver
myTree = BST()
myTree.insert(TNode('A'))
myTree.insert(TNode('B'))
myTree.insert(TNode('C'))
myTree.insert(TNode('D'))
myTree.insert(TNode('E'))
myTree.insert(TNode('F'))
myTree.insert(TNode('G'))

found = myTree.search(TNode('D'))

if found is not None:
	print(found.data)
else: 
	print("node doesn't exist in this tree")