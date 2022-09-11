# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val: 
            small, large = p, q  
        else: 
            small, large = q, p
        
        
        def dfs(node):
            if not node:
                return None
            
            if small.val < node.val < large.val:
                return node
            
            if large is node or small is node:
                return node
                       
            return dfs(node.left) or dfs(node.right)
                
        return dfs(root)
        
                