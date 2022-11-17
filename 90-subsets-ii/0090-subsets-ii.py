class Solution:
    def copyAndAdd(self, nums):
        subsets = [[]]
        s, e, prev = 0, 0, None
        for n in sorted(nums):
            temp = []
            if not prev or prev != n:
                s = 0
            e = len(subsets)
    
            for i in range(s, e):
                temp.append(subsets[i] + [n])
                
            prev, s = n, len(subsets)
            subsets.extend(temp)
        return subsets        
    
    
    def cascade(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]] 
        s, e, prev = 0, 0, None
        
        for n in sorted(nums):
            if prev:
                s = 0 if prev != n else e + 1
            e = len(subsets) - 1
            
            for i in range(s, e + 1):
                subsets.append(subsets[i] + [n])
            
            prev = n
            
        return subsets
    
    def incrementalLength(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, track):
            subsets.append(track)
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i+1, track + [nums[i]])
        
        nums.sort()
        subsets = []
        backtrack(0, [])
        return subsets
                     
                     
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return self.copyAndAdd(nums)
