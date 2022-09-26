class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        f2, f1 = 0, 1
        for _ in range(2, n+1):
            f2, f1 = f1, f1 + f2    
        return f1
    