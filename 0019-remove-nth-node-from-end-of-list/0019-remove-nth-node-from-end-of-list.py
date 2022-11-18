# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None            

        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        
        """
        1->2->3->4->5], n=2 => [1,2,3,5]
                2nd 1st
        
        - To delete 2nd, we need pointer to be on 3rd
        - so we let fast to mpve forward (n+1) steps, in advance. 
        """
        for _ in range(n+1): # if n=2, [0,1,2]
            if fast is None: 
                return dummy.next
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next        
    