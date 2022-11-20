# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        (1) lengths of l1 and l2 are same
        (2.1) lengths of l1 and l2 are different
            (2.2) carry carries on as the value for longer list is 9 
            (2.3) the last node has carry, so, a new node needs to be created.  
        """
        if not l1: return l2
        if not l2: return l1
        
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2:
            # If lengths are different, then, let it be 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            n, carry = sum % 10, sum // 10            
            cur.next = ListNode(n)
            
            # if lengths are different, then, step forward only the shorter one
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
            cur = cur.next 
            
        # if the last node has carry, new node is attached. 
        if carry: cur.next = ListNode(carry)

        return dummy.next         
        