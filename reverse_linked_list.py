"""
node.next is the "next arrow"

node.prev is the "prev arrow"

https://stackoverflow.com/questions/17897204/explanation-for-this-symbol-in-linked-list
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    previous_node, current_node = None, head
	
	while current_node:
		next_node = current_node.next
		current_node.next = previous_node #pick left arrow and point it to previous_node
		previous_node = current_node
		current_node = next_node
		
	return previous_node