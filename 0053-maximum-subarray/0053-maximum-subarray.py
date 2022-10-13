class Solution:
    
    def shortform(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        
        maxSum, curSum = nums[0], nums[0]

        for n in nums[1:]:
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
            
        return maxSum
    
    def bruteforce(self, nums: List[int]) -> int:
        maxSum = -math.inf

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                maxSum = max(max_subarray, current_subarray)    
        return maxSum
    
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cursum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if cursum < 0:
                cursum = nums[i]
            else: 
                cursum += nums[i]
            maxsum = max(cursum, maxsum)
        return maxsum