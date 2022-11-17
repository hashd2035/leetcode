class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for n in nums:
            heappush(minheap, n)
            if len(minheap) > k:
                heappop(minheap)
        return minheap[0]