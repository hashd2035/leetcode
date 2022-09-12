class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity): 
            daysIf, total = 1, 0
            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    daysIf += 1
                    if daysIf > days:
                        return False
            return True
        
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            m = lo + (hi - lo) // 2
            if canShip(m):
                hi = m
            else:
                lo = m + 1
        return lo
        