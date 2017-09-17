#Compare two strings represented as linked lists

from classes import Node, LinkedList

def compare(list1, list2):

	#stop when one list is empty or characters dont match
	while (list1 and list2 and list1.data == list2.data):
		list1 = list1.next
		list2 = list2.next

	#check mismatched characters
	if (list1 and list2):
		print("Lists similar up until: ", list1.data, list2.data)
		return
	if (list1 and not list2):
		print("List 1 is a longer word")
		return
	if (list2 and not list1):
		print("List2 is a longer word")
		return
	print("These two lists represent the same word")
	return

list1 = LinkedList()
phrase1 = "helloworld"
for c in phrase1:
	list1.append(Node(c))
list1.printList()

list2 = LinkedList()
phase2 = "helloworld"
for c in phase2:
	list2.append(Node(c))
list2.printList()

compare(list1.head, list2.head)