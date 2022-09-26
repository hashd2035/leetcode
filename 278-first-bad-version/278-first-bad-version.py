# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 1, n
        while i < j:
            m = i + (j - i)//2
            if isBadVersion(m):
                j = m
            else:
                i = m+1
        return j