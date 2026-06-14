# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        res = dummy
        slow = dummy
        fast = dummy

        i = 0
        while i < n:
            fast = fast.next
            i+=1
        print(fast.val)
        slow_prev = dummy
        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next

        slow_prev.next = slow.next

        return res.next
        