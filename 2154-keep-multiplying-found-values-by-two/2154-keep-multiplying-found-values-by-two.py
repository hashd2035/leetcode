class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == original:
                original = original * 2
        return original