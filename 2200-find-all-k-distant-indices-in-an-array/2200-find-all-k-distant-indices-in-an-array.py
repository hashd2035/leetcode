class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        for i, ni in enumerate(nums):
            for j in range(len(nums)):
                if abs(i - j) <= k and nums[j] == key:
                    ans.append(i)
        return list(set(ans))