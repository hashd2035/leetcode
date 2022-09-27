class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 5:21
        w, r = 0, 0
        while r < len(nums):
            if nums[r] == nums[w]:
                r += 1
            else:
                w += 1
                nums[w] = nums[r]
                r += 1
        return w+1