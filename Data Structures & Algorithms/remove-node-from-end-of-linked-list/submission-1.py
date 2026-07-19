# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        diff = 0

        dummyNode = ListNode(0, head)
        cur1 = dummyNode
        cur2 = dummyNode

        while diff != n:
            cur2 = cur2.next
            diff += 1
        
        while cur2.next:
            cur1 = cur1.next
            cur2 = cur2.next
        
        cur1.next = cur1.next.next

        return dummyNode.next