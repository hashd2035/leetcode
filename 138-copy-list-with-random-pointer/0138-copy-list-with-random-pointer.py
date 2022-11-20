"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ht = { None: None }
        """
        Note that an object can be a key for the hashtable
        `None: None` has to be explicitly called out
        """

        # Create all the nodes first
        cur = head
        while cur:
            ht[cur] = Node(cur.val)
            cur = cur.next 
            
        # Then, link all the nodes
        cur = head
        while cur:
            copy = ht[cur]
            copy.next = ht[cur.next] 
            copy.random = ht[cur.random] 
            cur = cur.next 
            
        # Use hashtable to return the copied head
        return ht[head]
            
            
        
        