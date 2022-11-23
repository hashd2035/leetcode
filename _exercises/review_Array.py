"""
Easy
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n 

        w, r = 0, 1
        for r in range(1, len(nums)):
            if nums[w] < nums[r]:
                w += 1
            nums[w] = nums[r]
        return w + 1

"""
Medium
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
"""
Easy
1925. Count Square Sum Triples
https://leetcode.com/problems/count-square-sum-triples/
"""
class Solution:
    def countTriples(self, n: int) -> int:
        

"""
Easy
2068. Check Whether Two Strings are Almost Equivalent
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
"""
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:


"""
Medium
811. Subdomain Visit Count
https://leetcode.com/problems/subdomain-visit-count/
"""
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:



"""
Easy
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

"""
Medium
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


"""
Easy
1. Two Sum
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:



"""
Medium
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


"""
Easy
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


"""
Medium
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


"""
Easy
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:


"""
Easy
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:



"""
Easy
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
    def add(self, val: int) -> int:

"""
Easy
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

"""
Easy
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:


"""
Easy
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

"""
Medium
77. Combinations
https://leetcode.com/problems/combinations/
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

"""
Medium
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    def prefixsum(self, nums):

"""
Medium
31. Next Permutation
https://leetcode.com/problems/next-permutation/
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:



"""
Medium
39. Combination Sum
https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        

"""
Medium
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


"""
Hard
51. N-Queens
https://leetcode.com/problems/n-queens/
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
"""
Medium
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        