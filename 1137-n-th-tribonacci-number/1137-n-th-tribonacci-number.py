class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2:
            return t[n]

        for _ in range(3, n+1):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
            """
            01[124]7
            
            """
        return t[2]
        