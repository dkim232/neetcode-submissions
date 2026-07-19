# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. find middle
        #2. reverse only second half
        #3. interleave first half with second half

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #slow is at the middle now
        #slow points to start of 
        prev = None
        secondHalf = slow.next

        slow.next = None

        while secondHalf:
            next = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = next

        
        #prev points to head of reversed LL
        while head and prev:
            curNext = head.next
            head.next = prev
            prev = prev.next
            head.next.next = curNext

            head = curNext

        
        