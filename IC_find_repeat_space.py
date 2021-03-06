"""
Find a duplicate, Space EditionTM. We have a list of integers, where:
1. The integers are in the range 1..n 2. The list has a length of n + 1
It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.
Write a function which  nds an integer that appears more than once in our list.
(If there are multiple duplicates, you only need to  nd one of them.)
We're going to run this function on our new, super-hip MacBook Pro With Retina DisplayTM. Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So we need to optimize for space!

Gotchas
We can do this in O(1) space.
We can do this in less than O(n2) time while keeping O(1) space.
We can do this in O(n lg n) time and O(1) space.
We can do this without destroying the input.
Most O(n lg n) algorithms double something or cut something in half. How can we rule out half of the numbers each time we iterate through the list?

"""

def find_duplicate(numbers):
    seen = []
    for num in numbers:
        if num not in seen:
            seen.append(num)
        else:
            seen.remove(num)
    if seen:
        return num
    else:
        return print("No Duplicate")

numbers = [1,2,3,3,3]

print(find_duplicate(numbers))

