class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # [1,3,5,6]
        lo, hi = 0, len(nums)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if nums[m] == target: 
                return m
            if target < nums[m]:
                hi = m
            else:
                lo = m + 1
        return lo
    
                