class Solution:
    """
    aab [a][a][b], [aa][b]
    a   [a]
    """

        
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True        
        
        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return 
                
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
                
        dfs(0)
        return res