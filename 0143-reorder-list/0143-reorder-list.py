# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Find Middle
        slow, fast = head, head.next 
        while fast:
            slow = slow.next 
            fast = fast.next 
            if fast:
                fast = fast.next 
            else:
                break
            
        # Reverse
        prev, cur = None, slow
        while cur:
            temp = cur.next 
            cur.next = prev
            prev, cur = cur, temp 
            
        # Reorder
        cur, L1, L2, toggle = head, head, prev, True
        while cur:
            if toggle:
                L1 = L1.next 
                cur.next = L2
            else:
                L2 = L2.next 
                cur.next = L1
            cur = cur.next 
            toggle = not toggle
            
        return head
                