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
        


"""
Easy
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
"""

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                # note we don't need to update prev. Watch neetcode
            else:
                prev = cur  
            cur = cur.next
                
        return dummy.next 

"""
Medium
0019-remove-nth-node-from-end-of-list
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1->2->3->4->5, n=2
                2nd 1st
              s        f
        
        - Need n+1 th node
        - node = node.next.next 
        """
        slow, fast = head, head 
        for _ in range(n+1):
            if not fast:
                return head 
            fast = fast.next 

        while fast:
            slow = slow.next 
            fast = fast.next 

        slow = slow.next.next 
        return head



"""
Easy
0141-linked-list-cycle 
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next 
        while fast and fast.next:
            if slow == fast:
                return True
            slow, fast = slow.next, fast.next.next
        return False 

"""
Medium
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        
"""
Medium
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

[1, n] inclusive : n+1 integers
- without modifying the array
- constant extra space

Related: Linked List Cycle I and II
"""
class Solution:
    # Array as hashset
    def findDuplicate(self, nums: List[int]) -> int:
        """
        """
        for i in range(len(nums)):
            """
            1. the 'number at index' has to be i+1
                otherwise, swap 
            2. if the number to be swapped is already in place, return 
            """
            while nums[i] != i+1:
                idx = nums[i]-1
                if nums[i] == nums[idx]:
                    return nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]
        return None

    # Watch neetcode solution (https://www.youtube.com/watch?v=wjYnzkAhcNk)
    def usingFastAndSlowPointer(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow = slow2:
                return slow 

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
        ht = {}

        cur = head
        while cur:
            ht[cur] = Node(cur.val)
            cur = cur.next 

        cur = head
        while cur:
            ht[cur].next = ht[cur.next]
            ht[cur].random = ht[cur.random]
            cur = cur.next 

        return ht[head]

"""
Medium
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""
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




"""
Medium
146. LRU Cache
https://leetcode.com/problems/lru-cache/
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
https://leetcode.com/problems/merge-k-sorted-lists/
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

"""
Hard
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

