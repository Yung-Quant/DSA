class TNode:

	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data

class Tree:

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