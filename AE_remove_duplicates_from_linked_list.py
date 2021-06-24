# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	currentNode = linkedList
	while currentNode != None:
		nextNode = currentNode.next
		while nextNode != None and nextNode.value == currentNode.value:
			nextNode = nextNode.next
		
		currentNode.next = nextNode
		currentNode = nextNode
		
	return linkedList
    
#O(n) time | O(1) space where n is the number of nodes in the LL
