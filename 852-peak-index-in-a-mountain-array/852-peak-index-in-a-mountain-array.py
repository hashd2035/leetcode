class Solution:
    def linearSearch(self, arr):
        for i in range(len(arr)):
            if i-1 >= 0 and i+1 <len(arr) and arr[i-1] < arr[i] > arr[i+1]:
                return i
        return -1
    
    def binarySearch(self, arr):
        def cond(val):
            return 
        
        lo, hi = 0, len(arr)
        
        while lo < hi:
            m = lo + (hi - lo) // 2
            if m >= 1 and m < len(arr)-1 and arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m] < arr[m+1]:
                lo = m + 1                
            else:
                hi = m
        return lo
    
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.binarySearch(arr)