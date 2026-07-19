# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        numElements = 0

        cur = head

        while cur:
            numElements += 1
            cur = cur.next
        
        indexToRemove = numElements - n

        #on n-1th element, link it to n+1th element
        
        cur2 = ListNode(0, head)
        res = cur2
        index = 0
        while cur2:
            if index == indexToRemove:
                cur2.next = cur2.next.next
            index += 1
            cur2 = cur2.next
        
        return res.next