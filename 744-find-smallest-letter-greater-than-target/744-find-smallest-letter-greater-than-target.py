class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if letters[m] > target:
                hi = m
            else:
                lo = lo + 1
                
        return letters[0] if lo == len(letters) else letters[lo]