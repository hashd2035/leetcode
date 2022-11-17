class Solution:
    def bfs(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,3]
        
        1. start with []
        2. add 1 to all positions: [1]
        3. add 2 to all positions: [1,2], [2,1]
        4. add 3 to all positions: [3,1,2], [1,3,2], [1,2,3]
                                   [3,2,1], [2,3,1], [2,1,3]
        """
        ans = [[]]
        for i in range(len(nums)):
            tempAns = []           
            while ans:
                perm = ans.pop()    
                tempAns.append([nums[i]] + perm)
                for j in range(1, len(perm)+1):                        
                    tempAns.append(perm[:j] + [nums[i]] + perm[j:])
            ans = tempAns                
        return ans
    
    def backtracking(self, nums: List[int]) -> List[List[int]]:
        def backtrack(track, choices):
            if len(track) == len(nums):
                ans.append(track)
                return
            for i in range(len(choices)):
                remaining = choices[:] 
                sel = remaining.pop(i)
                backtrack(track+[sel], remaining)

        ans = []
        backtrack([], nums)
        return ans

    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtracking(nums)
    