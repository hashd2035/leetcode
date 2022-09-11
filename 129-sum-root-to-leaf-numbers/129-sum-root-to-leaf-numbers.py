# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        
        def dfs(node: Optional[TreeNode], path: List[str]):
            if node is None:
                return 
            if node.left is None and node.right is None:
                numbers.append(path + [str(node.val)])
                return 
            
            dfs(node.left, path + [str(node.val)])
            dfs(node.right, path + [str(node.val)])
            
        dfs(root, [])
        
        _sum = 0
        for p in numbers:
            n = ''.join(p)
            _sum += int(n)
        
        
        return _sum