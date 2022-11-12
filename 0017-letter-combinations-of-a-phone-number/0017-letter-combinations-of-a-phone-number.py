class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        lchars = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        ans = []
        def dfs(i, track):
            if len(track) == len(digits):
                ans.append(''.join(track))
                return 
            
            d = digits[i]
            for c in lchars[d]:
                dfs(i+1, track + [c])
            
        dfs(0, [])
        return ans