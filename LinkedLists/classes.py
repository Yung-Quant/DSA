#class file for linked list 

class Node:

	#constructor to initialize node object
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		print(self.data)

class LinkedList:

	def __init__(self):
		self.head = None

	#append node
	def append(self, new_node):
		#empty LList case
		if self.head is None:
			new_node.next = self.head
			self.head = new_node
			return
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = new_node
			return


	def sortedInsert(self, new_node):
		#this assumes a sorted list
		#special case where linked list is empty
		if self.head is None:
			new_node.next = self.head
			self.head = new_node

		#special case where there's only one node (ie head at end)
		elif self.head.data >= new_node.data:
			new_node.next = self.head
			self.head = new_node

		else:
			#locate the node BEFORE insertion
			current = self.head
			while(current.next is not None and current.next.data < new_node.data):
				current = current.next

			new_node.next = current.next
			current.next = new_node

	#insert node at begining
	def prepend(self, new_node):
		new_node.next = self.head
		self.head = new_node

	#remove last node
	def pop(self):
		#check if empty
		if self.head is None:
			print("the list is empty, nothing to pop()!")
			return
		#check if only one node in Llist
		elif self.head.next is None:
			self.head = None
			return
		#common case
		current = self.head
		while current.next.next is not None:
			current = current.next
		current.next = None
		return


	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def deleteNode(self, dNode):
		#case where head is to be deleted
		if dNode == self.head:
			self.head = self.head.next

		#case when head is not to be deleted
		else:
			current = self.head
			while current.next is not dNode:
				current = current.next
			current.next = current.next.next
			print("deleted: " + str(dNode.data) )








