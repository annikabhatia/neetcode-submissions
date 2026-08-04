# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reach the nth element of the linked list (set a counter and increment that counter, once it is greater than n), set the prev = prev.next.next to remove that element from the linked list. make sure to continously update current and count with every element we loop through.
        current = head
        dummy = ListNode(0, head)
        prev = dummy
        
        count = 1

        while current:

            #ex) when n=2, this actually means its the 3rd element
            if count > n:
                prev = prev.next
            current = current.next
            count+=1

        #we only do this condition once if condition is satisfied, and this gets rid of the element that we need.
        prev.next = prev.next.next
            
        
        return dummy.next


        