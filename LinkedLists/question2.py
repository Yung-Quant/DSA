#Given a Singly Linked List, write a function to delete a given node. Your function must follow following constraints:

#You may assume that the Linked List never becomes empty.

from classes import Node, LinkedList

llist = LinkedList()
llist.append(Node(5))
x = Node(15)
llist.prepend(x)
llist.prepend(Node(16))
llist.printList()
llist.deleteNode(x)
llist.printList()
