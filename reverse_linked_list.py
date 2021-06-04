"""
node.next is the "next arrow"

node.prev is the "prev arrow"

https://stackoverflow.com/questions/17897204/explanation-for-this-symbol-in-linked-list
"""
#leetcode 206
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
    previous_node, current_node = None, head
	
	while current_node:
        #current_node.next is the arrow
		next_node = current_node.next #points arrow to next node therefore right arrow
		current_node.next = previous_node #points arrow to previous_node therefore left arrow
		previous_node = current_node
		current_node = next_node
		
	return previous_node

def reverseLL(head):
    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev