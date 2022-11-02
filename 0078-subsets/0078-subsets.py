class Solution:
    def cascade(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            tempset = []
            for subset in subsets:
                tempset.append(subset + [n])
            subsets.extend(tempset)
        return subsets

    def incrementalLength(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(start, track):
            ans.append(track)
            for i in range(start, len(nums)):
                backtrack(i+1, track + [nums[i]])
                
        backtrack(0, [])
        return ans
                    
    
    def skipOrSelect(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(i, track):
            if i >= len(nums):
                ans.append(track)
                return
            
            backtrack(i+1, track)
            backtrack(i+1, track+[nums[i]])
            
        backtrack(0, [])
        return ans
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.incrementalLength(nums)