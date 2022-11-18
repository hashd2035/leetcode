class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        old_len = len(nums)
        new_len = len(nums) * 2
        ans = [0] * new_len
        for i in range(new_len):
            if i < old_len:
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-old_len]
        return ans
        # return nums * 2