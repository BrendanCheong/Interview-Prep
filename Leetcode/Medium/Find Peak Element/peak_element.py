from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        This is binary search but modified. We want to find the bitonic peak in O(log n) time.
        We can find the peak by checking the left and right of the middle.
        We must go in the direction of the larger number when checking left and right.
        so if: 1, 2, 3, 4, 1 -> we must go right, as middle is 3, 4 is larger, so move left pointer
        if: 1, 5, 3, 2, 1 -> middle is 3, 5 is larger, so move right pointer.
        Binary search is about closing the pointers to find the middle.
        """
        left = 0
        right = len(nums)-1

        # 0. has to be left < right not left <= right or else its out of bounds
        # if left <= right, then do this:
        # if (left == right):
        #         return mid
        while left < right:
            
            mid = (left + right) // 2
            
    
            # 1. since it can be multiple peaks, we just pick a side, we just say that if right side is bigger, move left towards right. Ignore left side
            # this also counters the fact that we can be out of bounds of the array
            # this also accounts for arrays len(nums) < 3. where the middle is always gonna within bounds
            if (nums[mid + 1] > nums[mid]):
                left = mid + 1
            elif (nums[mid - 1] > nums[mid]):
                right = mid - 1
            # 2. check for the case where the middle is the answer
            elif (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                return mid
        return left
            
        