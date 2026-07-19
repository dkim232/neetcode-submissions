"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashTable = {}
        cur = head
        while cur:
            newNode = Node(cur.val)
            hashTable[cur] = newNode
            cur = cur.next
        
        hashTable[None] = None
        
        cur = head
        while cur:
            copy = hashTable[cur]
            copy.next = hashTable[cur.next]
            copy.random = hashTable[cur.random]
            cur = cur.next
        
        return hashTable[head]