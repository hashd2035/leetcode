class Solution:
    # Array as hashset
    def findDuplicate(self, nums: List[int]) -> int:
        """
        """
        for i in range(len(nums)):
            """
            1. the 'number at index' has to be i+1
                otherwise, swap 
            2. if the number to be swapped is already in place, return 
            """
            while nums[i] != i+1:
                idx = nums[i]-1
                if nums[i] == nums[idx]:
                    return nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]
        return None

    # Watch neetcode solution (https://www.youtube.com/watch?v=wjYnzkAhcNk)
    def usingFastAndSlowPointer(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow = slow2:
                return slow         