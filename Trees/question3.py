#In order, pre order and post order traversal

from classes import TNode, BST


#driver
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

myTree.IOTrav(myTree.root)
print("\n")
myTree.PoOTrav(myTree.root)
print("\n")
myTree.PreOTrav(myTree.root)
print("\n")
