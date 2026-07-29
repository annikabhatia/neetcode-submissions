# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() 
        current = dummy #to iterate through linked lists
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        #if there are leftover nodes in either l1 or l2 that do not need to be compare, they can just get attached to end of merged linked list
        current.next = l1 if l1 else l2
        
        return dummy.next