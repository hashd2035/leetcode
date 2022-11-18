# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge1(self, L1, L2):
        cur = head = L1
        toggle = True
        while cur:
            if toggle:
                L1 = L1.next 
                cur.next = L2
            else:
                L2 = L2.next 
                cur.next = L1
            cur = cur.next 
            toggle = not toggle

    def merge2(self, L1, L2):
        while L1 and L2:
            temp1, temp2 = L1.next, L2.next
            L1.next = L2
            L2.next = temp1            
            L1, L2 = temp1, temp2        
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # Reverse
        prev, cur = None, slow
        while cur:
            temp = cur.next 
            cur.next = prev
            prev, cur = cur, temp 
            
        # Reorder
        """
        Do not return anything, modify head in-place instead.
        """
        self.merge2(head, prev)
                