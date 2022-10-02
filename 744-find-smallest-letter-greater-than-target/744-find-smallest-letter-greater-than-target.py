class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        
        """
        # if target >= letters[-1]:
        #     letters[0]
        
        lo, hi = 0, len(letters)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if letters[m] > target:
                hi = m
            else:
                lo = lo + 1
                
        
        if lo == len(letters):
            return letters[0]
        else:
            return letters[lo]