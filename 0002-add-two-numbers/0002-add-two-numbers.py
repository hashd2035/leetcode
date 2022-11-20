# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2->4->3
        5->6->4
        7->0->8
        """
        if not l1: return l2
        if not l2: return l1
        
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            n = sum % 10 
            carry = sum // 10
            cur.next = ListNode(n)
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
            cur = cur.next 
            
        if carry: cur.next = ListNode(carry)

            
        return dummy.next 
        
        