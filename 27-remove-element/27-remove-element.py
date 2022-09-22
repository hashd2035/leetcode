class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0
        # for x in nums:
        #     if x != val:
        #         nums[i] = x
        #         i += 1
        # return i
        if not nums:
            return 0
        w = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[w] = nums[r]
                w += 1
        return w 
    