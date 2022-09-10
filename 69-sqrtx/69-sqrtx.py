class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: 
            return x
        
        lo, hi = 0, x
        while lo < hi:
            m = lo + (hi - lo) //2
            
            # if the condition is true, discard
            if m * m == x:
                return m
            elif m * m > x: 
                hi = m
            else:
                lo = m + 1
        return lo - 1
