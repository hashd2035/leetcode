class Solution:
    def bisect_right(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            m = left + (right - left) // 2
            if target < nums[m]:
                right = m
            else:
                left = m + 1
        return left
    
    def bisect_left(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            m = left + (right - left) // 2
            if nums[m] < target:
                left = m+1
            else:
                right = m
        return left

    def binary_search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            m = left + (right - left) // 2
            if target == nums[m]:
                return m
            if target < nums[m]:
                right = m-1
            else:
                left = m+1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        #return self.binary_search(nums, target)    
        pt = self.bisect_left(nums, target) 
        return pt if pt < len(nums) and nums[pt] == target else -1