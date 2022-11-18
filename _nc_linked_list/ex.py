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
    def reorderList(self, head: Optional[ListNode]) -> None:
        
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

