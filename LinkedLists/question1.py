#Given a linked list which is sorted, insert a linked while maintaining sort


from classes import Node, LinkedList
# Driver program
llist = LinkedList()
new_node = Node(5)
llist.sortedInsert(new_node)
new_node = Node(10)
llist.sortedInsert(new_node)
new_node = Node(7)
llist.sortedInsert(new_node)
new_node = Node(3)
llist.sortedInsert(new_node)
new_node = Node(1)
llist.sortedInsert(new_node)
new_node = Node(9)
llist.sortedInsert(new_node)
new_node = Node(2)
llist.sortedInsert(new_node)
print("Create Linked List")
llist.printList()