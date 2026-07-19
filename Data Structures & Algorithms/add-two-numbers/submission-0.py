# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        cur = dummyNode
        carryOver = 0

        while l1 or l2 or carryOver != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sumval = val1 + val2 + carryOver
            print(sumval)
            carryOver = 0

            if sumval >= 10:
                carryOver = sumval // 10
                sumval = sumval % 10
            
            newNode = ListNode(sumval)
            cur.next = newNode
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        cur.next = None

        return dummyNode.next