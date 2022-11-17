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
        
        # get mid
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        # reverse
        pre, second = None, slow.next
        slow.next = None
        while second:
            temp = second.next
            second.next = pre
            pre = second
            second = temp
        
        # merge
        first, second = head, pre
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            
            first, second = temp1, temp2
        