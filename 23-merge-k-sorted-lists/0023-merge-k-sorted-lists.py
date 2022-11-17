# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        ListNode.__eq__ = lambda self, other: self.val == other.val
        
        if not lists: return None
        
        merged = []

        for root in lists:
            if root:
                heappush(merged, root)
            
        nodeHead, nodeTail = None, None
        while merged:
            node = heappop(merged)
            
            if not nodeHead:
                nodeHead = node
                nodeTail = node
            else:
                nodeTail.next = node
                nodeTail = nodeTail.next
            
            if node and node.next: 
                heappush(merged, node.next)
            
        return nodeHead