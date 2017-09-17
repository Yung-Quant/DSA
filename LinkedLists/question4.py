#Add two numbers represented by a linked list
#list 1: 4->5->0
#list 2: 5->5->0
#result: 1->0->0->0

from classes import Node, LinkedList

def addNumbers(list1, list2):
	#change lists to strings
	num1 = ""
	num2 = ""
	while(list1 or list2):
		if list1 is not None:
			num1 = num1 + str(list1.data)
			list1 = list1.next
		if list2 is not None:
			num2 = num2 + str(list2.data)
			list2 = list2.next
	sum = int(num1) + int(num2)
	print(int(num1), int(num2), sum )



#driver
list1 = LinkedList()
list1.prepend(Node(0))
list1.prepend(Node(5))
list1.prepend(Node(4))
list1.prepend(Node(5))

list2 = LinkedList()
list2.prepend(Node(5))
list2.prepend(Node(5))


addNumbers(list1.head, list2.head)