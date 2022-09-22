class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        jlist = [j for j in range(len(nums)) if nums[j] == key]
        
        for i in range(len(nums)):
            for j in jlist:
                if abs(i-j) <= k:
                    ans.add(i)
                    
        return list(ans)