class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m = len(nums) // 2
        ans = []
        for i, j in zip(range(m), range(m, len(nums))):
            ans.append(nums[i])
            ans.append(nums[j])
            
        return ans