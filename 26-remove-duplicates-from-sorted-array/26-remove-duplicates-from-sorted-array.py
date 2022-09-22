class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n, w = len(nums), 0
        if n <= 1: return n
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                w += 1
                nums[w] = nums[r]
        return w + 1