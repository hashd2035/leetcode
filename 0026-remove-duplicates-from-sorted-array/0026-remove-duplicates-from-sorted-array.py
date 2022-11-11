class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        w = 1
        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:
                nums[w] = nums[r]
                w += 1
        
        return w