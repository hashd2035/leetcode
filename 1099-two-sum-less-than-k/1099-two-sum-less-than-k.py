class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        #39
        def bisect(target, lo, hi):
            while lo < hi:
                m = lo + (hi - lo) // 2
                if target <= nums[m]:
                    hi = m
                else:
                    lo = m + 1
            return lo-1
                
        n = len(nums)
        nums.sort()
        max_sum = -1
        for i in range(n):
            j = bisect(k-nums[i], i+1, n)
            if i < j:
                max_sum = max(max_sum, nums[i]+nums[j])
        return max_sum