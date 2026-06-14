# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = None
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_part = slow.next
        slow.next = None
        second_part = self.reverse(second_part)

        first_part = head
        while first_part and second_part:
            first_part_next = first_part.next
            second_part_next = second_part.next


            first_part.next = second_part
            second_part.next = first_part_next
            first_part = first_part_next
            second_part = second_part_next


    def reverse(self, head):

        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        