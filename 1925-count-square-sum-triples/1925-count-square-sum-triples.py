class Solution:
    def bruteforce(self, n):
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c = sqrt(a*a + b*b)
                if c <= n and not (c%1):
                    count += 1
        return count
    
    def countTriples(self, n: int) -> int:
        return self.bruteforce(n)