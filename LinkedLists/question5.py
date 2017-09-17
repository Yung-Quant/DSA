#Merge a linked list into another linked list at alternate positions


from classes import Node, LinkedList

def mergeListsALT(list1,list2):
	merged = LinkedList()
	listbool = 1 #start with list one, alternate for append operation
	while list1 or list2:
		if listbool == 1:
			if list1:
				merged.append(Node(list1.data))
				list1 = list1.next
			listbool = 2

		elif listbool == 2:
			if list2:
				merged.append(Node(list2.data))
				list2 = list2.next
			listbool = 1
	return merged







#driver
list1 = LinkedList()
list1.append(Node(1))
list1.append(Node(3))
list1.append(Node(5))
list1.append(Node(7))

list2 = LinkedList()
list2.append(Node(2))
list2.append(Node(4))
list2.append(Node(6))
list2.append(Node(8))

list3 = mergeListsALT(list1.head, list2.head)
list3.printList()
