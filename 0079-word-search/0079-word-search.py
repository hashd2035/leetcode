class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        
        def dfs(i, r, c):
            if i == len(word):
                return True

            if 0 > r or r >= m or 0 > c or c >= n: 
                return False
            
            if board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r,c))
            
            for dr, dc in DIRECTIONS:
                if dfs(i+1, r+dr, c+dc):
                    return True
            
            visited.remove((r,c))
            
            return False
            
        for r in range(m):
            for c in range(n):
                if board[r][c] != word[0]:
                    continue
                    
                if dfs(0, r, c):
                    return True
                
        return False
        

                
                