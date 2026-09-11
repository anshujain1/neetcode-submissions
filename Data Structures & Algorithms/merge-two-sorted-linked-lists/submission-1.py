# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =p= ListNode()
        curr = list1
        curr2 = list2
        while curr and curr2:
            if curr.val >= curr2.val:
                p.next = curr2
                curr2 = curr2.next
            else:
                p.next = curr
                curr = curr.next
            p = p.next

        p.next = curr or curr2
        return dummy.next
        
                