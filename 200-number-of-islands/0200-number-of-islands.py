class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 
            
            if grid[r][c] != '1' or (r, c) in visited:
                return 
            
            visited.add((r, c))
            
            for dr, dc in DIRS:
                dfs(r+dr, c+dc)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
                    
        return count