# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Easy
226. Invert Binary Tree
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = root.right, root.left 
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

"""
Easy
100. Same Tree
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p  or not q: return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Easy
572. Subtree of Another Tree
"""
class Solution:
    def isSameTree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    


"""
Easy
104. Maximum Depth of Binary Tree
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0
        
        return 1 + max(left, right)    


"""
Easy
110. Balanced Binary Tree
"""
class Solution:    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


"""
Easy
543. Diameter of Binary Tree
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        


"""
Easy
112. Path Sum
https://leetcode.com/problems/path-sum/
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


