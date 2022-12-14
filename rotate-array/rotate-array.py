class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) <= 1 or len(nums) == k:
            return 
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k % len(nums)
            
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
        
    def reverse(self, nums, i, j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1