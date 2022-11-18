# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Easy
0206-reverse-linked-list 
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
      

"""
Easy
21-merge-two-sorted-lists
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
"""
Medium
0143-reorder-list
https://leetcode.com/problems/reorder-list/

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

"""
class Solution:
    """
    L0 → L1 → L2 → → → → Ln - 2 → Ln - 1 → Ln

    - Use slow, fast to find the middle
    - reverse from middle to end
    - merge
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        # reverse
        pre, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp 

        # reorder
        L1, L2 = head, prev 
        cur, toggle = head, True 
        while L1 and L2:
            if toggle:
                L1 = L1.next 
                cur.next = L2 
            else:
                L2 = L2.next
                cur.next = L1 
            cur = cur.next 
            toggle = not toggle
        
        return head 


"""
Easy
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
"""

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head or head.val == val:
            return None
        
        prev, cur = head, head.next 
        while cur:
            if cur.val == val:
                prev.next = cur.next 
            prev, cur = cur, cur.next  
        
        return head

"""
Medium
0019-remove-nth-node-from-end-of-list
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


"""
Medium Walmart
138. Copy List with Random Pointer
"""
# Definition for a Random Node.
class RNode:
    def __init__(self, x: int, next: 'RNode' = None, random: 'RNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[RNode]') -> 'Optional[RNode]':

"""
Medium
2. Add Two Numbers
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


"""
Easy
0141-linked-list-cycle 
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


"""
Medium
287. Find the Duplicate Number
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

"""
Medium
146. LRU Cache
"""
class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Hard
23-merge-k-sorted-lists
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

"""
Hard
25. Reverse Nodes in k-Group
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

