class Solution:
    """
    Approach #1 - Calculating how many steps to move in each direction --> Overcomplicates steps
    
    Approach #2 - Keep track of boundaries --> Still a bit overcomplicating

    Approach #3 - Keep track of visited --> Simpler (becomes the same ques as number of island)
    """
    
    ## Not working
    def approach1(self, matrix: List[List[int]]) -> List[int]:
#         ans = []
        
#         def goSpiral(r, c, m, n):
#             if m == 0 and n == 0:
#                 return 
            
#             # move right (r, c) .. (r+1, n-1)
#             for _ in range(n):
#                 ans.append(matrix[r][c])
#                 c += 1
#             c -= 1
            
#             # move down m-1
#             for _ in range(r+1, m):
#                 ans.append(matrix[r][c])
#                 r += 1            
#             r -= 1
            
#             # move left n-1
#             for _ in range(, m):
#                 ans.append(matrix[r][c])
#                 c -= 1
#             c += 1
            
#             # move up m-2
#             for _ in range(m):
#                 ans.append(matrix[r][c])
#                 r -= 1                
#             r += 1
            
#             goSpiral(r, c, m-1, n-1)
        
#         goSpiral(0, 0, len(matrix), len(matrix[0])) # (r, c) is the starting position
        
#         return ans
        pass
    
    ## Not working    
    def approach2(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        
        # move_right = lambda row, start, end : [matrix[row][col+d] for d in range(start, end)]
        # move_down =  lambda col, start, end : [matrix[row+1][col] for d in range(start, end)]
        # move_left =  lambda row, start, end : [matrix[row][col-d] for d in range(start, end)]
        # move_up =    lambda col, start, end : [matrix[row-1][col] for d in range(start, end)]
        
        r, c = 0, 0
        
        while len(ans) < m * n:
            ans.extend([matrix[r][d] for d in range(c, n)])
            # ans.extend(move_right(r, c, n))
            c += 1
            ans.extend([matrix[d][c] for d in range(r, m)])
            # ans.extend(move_down (c, r, m))
            m -= 1
            ans.extend([matrix[r][-d] for d in range(c, n)])
            # ans.extend(move_left (r, c, n))
            n -= 1
            ans.extend([matrix[-d][c] for d in range(r, m)])
            # ans.extend(move_up   (c, r, m))
            r += 1
        return ans
        
    def approach3(self, matrix: List[List[int]]) -> List[int]:
        self.DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)] # right, down, left, up
        m, n = len(matrix), len(matrix[0])
        self.ans, visited = [matrix[0][0]], set()
                
        def dfs(row, col):            
            visited.add((row, col))
            for dr, dc in self.DIRECTIONS:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    self.ans.append(matrix[row][col])
                    dfs(r, c)
            self.DIRECTIONS = self.DIRECTIONS[1:] + self.DIRECTIONS[:1]
            
        dfs(0, 0)
        return ans
    
    
    def anser(self, matrix):
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        self.ans = [matrix[0][0]]
        def dfs(row, col):
            visited.add((row, col))
            for r, c in self.dirs:
                new_r = r + row
                new_c = c + col
                if 0 <= new_r < len(matrix) and \
                0 <= new_c < len(matrix[0]) and (new_r, new_c) not in visited:
                    self.ans.append(matrix[new_r][new_c])
                    dfs(new_r, new_c)
                self.dirs = self.dirs[1:] + self.dirs[:1]
        dfs(0, 0)
        return self.ans
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.anser(matrix)