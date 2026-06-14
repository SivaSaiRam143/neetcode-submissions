# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        mov_head = head
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    # if head == None:
                    #     head = list1
                    #     mov_head = head
                    #     list1 = list1.next
                    # else:
                        mov_head.next = list1
                        mov_head = mov_head.next
                        list1 = list1.next
                elif list2.val <= list1.val:
                    # if head == None:
                    #     head = list2
                    #     mov_head = head
                    #     list2 = list2.next
                    # else:
                        mov_head.next = list2
                        mov_head = mov_head.next
                        list2 = list2.next
            elif list1:
                # if head == None:
                #     head = list1
                #     mov_head = head
                #     list1 = list1.next
                # else:
                    mov_head.next = list1
                    mov_head = mov_head.next
                    list1 = list1.next    
            elif list2:
                # if head == None:
                #     head = list2
                #     mov_head = head
                #     list2 = list2.next
                # else:
                    mov_head.next = list2
                    mov_head = mov_head.next
                    list2 = list2.next 

        return head.next                 
        