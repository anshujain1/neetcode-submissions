# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        second = slow.next
        slow.next = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        second = prev
        first = head 
        while first and second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
        
            
            
            
        