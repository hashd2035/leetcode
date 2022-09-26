class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        copy = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                copy.append(nums1[i])
                i += 1                
            else:
                copy.append(nums2[j])
                j += 1

        print("1", copy)
        copy.extend(nums1[i:m])        
        print("2", copy)
        copy.extend(nums2[j:n])        
        print("3", copy)

        i, k = m, 0
        
        for i in range(len(nums1)):
            nums1[i] = copy[i]
