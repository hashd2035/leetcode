class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # if m == 0 or n == 0:
            
        merged = []
        i, j = 0, 0
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        while i < m:
            merged.append(nums1[i])
            i += 1
            
        while j < n:
            merged.append(nums2[j])
            j += 1                     
        
        merged_len = m+n
        median = merged_len // 2
        if merged_len % 2 == 1:
            return merged[median]
        else:
            return (merged[median] + merged[median-1]) / 2
            
        
            
            
            