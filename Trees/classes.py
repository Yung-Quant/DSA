class TNode:

	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data

class BST:

	def __init__(self):
		self.root = None

	def insert(self, new_node):
		#if tree is empty
		if self.root is None:
			self.root = new_node

		else:
			current = self.root
			parent = None

			while True:
				parent = current

				#check for left child
				if(new_node.data < parent.data):
					current = current.left

					if(current is None):
						parent.left = new_node
						return
				#check for right child
				else:
					current = current.right
					if(current is None):
						parent.right = new_node
						return

	def search(self, sNode):

		current = self.root
		#check root
		if current is None:
			return None

		else:

			while current is not None and current.data != sNode.data:
				#move left
				if current.data  > sNode.data:
					current = current.left
				#move right
				else:
					current = current.right

		return current

	def IOTrav(self, node):
		if node is None:
			return
		self.IOTrav(node.left)#recur left 
		print(node.data)
		self.IOTrav(node.right)#recur right

	def PoOTrav(self, node):
		if node is None:
			return
		self.PoOTrav(node.left)#recur left
		self.PoOTrav(node.right)#recur right
		print(node.data)

	def PreOTrav(self, node):
		if node is None:
			return

		print(node.data)
		self.PreOTrav(node.left) #recur left
		self.PreOTrav(node.right) #recur right


