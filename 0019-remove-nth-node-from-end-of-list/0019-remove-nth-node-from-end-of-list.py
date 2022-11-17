# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode()
        dummy.next = head
        walker, runner = dummy, dummy

        count = 0
        while count <= n:
            if runner is None:
                return dummy.next
            runner = runner.next
            count += 1

        while runner is not None:
            runner = runner.next
            walker = walker.next

        walker.next = walker.next.next
        return dummy.next        