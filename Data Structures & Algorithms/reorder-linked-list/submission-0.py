# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get midpoint of 2 halves (cycle)
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None
        prev = None

        #reverse linked list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge linked list
        first = head
        second = prev
        #2nd half CAN be shorter (if odd # of values); only check for when second is NOT null
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2




        
