class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        """
        n = len(nums)
        aux = [-1]*(n+1)
        for n in nums:
            aux[n] = n
            
        print(aux)
        for i, n in enumerate(aux):
            if n == -1:
                return i
        
        return -1