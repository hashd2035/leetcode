class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h:
            return -1
        
        def canEatAllBananas(speed):
            hours = 0
            for pile in piles:
                hours += ceil(pile / speed)    
            return hours if hours <= h else 0
                    
        piles.sort()
        lo, hi = 1, piles[-1]

        while lo < hi:
            m = lo + (hi - lo) // 2
            if canEatAllBananas(m):
                hi = m
            else: 
                lo = m + 1
        return hi
            
        
                
        