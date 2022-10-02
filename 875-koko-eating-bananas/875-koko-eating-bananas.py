class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        # how many and at most a pile
        k = speed = 1..max(piles) 
        
        within h, but, max 
        
        curspeed = ceil(pile[i]/k)
        """
        minspeed = math.inf 
        lo, hi = 1, max(piles)+1

        while lo < hi:
            curspeed = lo + (hi - lo) // 2
            hours = sum([math.ceil(p/curspeed) for p in piles])            

            if hours <= h:
                minspeed = min(minspeed, curspeed)
                hi = curspeed
            else:
                lo = curspeed + 1
        return minspeed
                
