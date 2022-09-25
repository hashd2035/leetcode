class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        money=[1,2,3,1]
  
        """
        last, now = 0, 0
        for money in nums:
            last, now = now, max(last+money, now)
        return now 