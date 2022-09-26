class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg, pos = [], []
        for n in nums:
            if n < 0:
                neg.append(n*n)
            else:
                pos.append(n*n)
        
        neg.reverse()
        
        i, j, k = 0, 0, 0
        while i < len(neg) and j < len(pos):
            if neg[i] <= pos[j]:
                nums[k] = neg[i]
                i += 1 
            elif j < len(pos):
                nums[k] = pos[j]
                j += 1 
            k += 1

        while i < len(neg):
            nums[k] = neg[i]
            i += 1 
            k += 1            
            
        while j < len(pos):
            nums[k] = pos[j]
            j += 1 
            k += 1            

        return nums