# O(n + m) time | O(c) space
# where n is the number of characters, m is length of doc 
# and c is num of unique char in char string
def generateDocument(characters, document):
    # Write your code here.
    
	characterCount = {}
	
	for char in characters:
		if char in characterCount:
			characterCount[char] += 1
		else:
			characterCount[char] = 1
			
	for char in document:
		if char not in characterCount or characterCount[char] == 0:
			return False
		
		characterCount[char] -= 1
		
	return True
	
