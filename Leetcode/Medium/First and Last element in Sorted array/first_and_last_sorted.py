from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        This is a 2 O(log n) or O(log n) time algo with O(1) space
        """
        return [self.searchFirstLeft(nums, target), self.searchFirstRight(nums, target)]
    
    def searchFirstLeft(self, A: List[int], target: int) -> int:
        left, right = 0, len(A) - 1
        # start with a simple binary search
        while (left <= right):
            mid = (left + right) // 2
            
            if (A[mid] < target):
                # we must go right
                left = mid + 1
            elif (A[mid] > target):
                # we must go left
                right = mid - 1
            else:
                # now for the modifications to the binary search
                # what happens when we found the target?
                # it may not be the left most, so we have to keep going left until we find it
                if (mid - 1 < 0):
                    # if the A[mid] == target and going to left is out of bounds
                    # then the target is mid
                    return mid
                elif (A[mid - 1] != target):
                    # when going to the left is not the target, then mid is the target
                    # edge case of: 1, 10 , 10, 5,
                    return mid
                else:
                    # if not, we must keep going to the left side of mid until we find the 
                    # target
                    right = mid - 1
        return -1
    def searchFirstRight(self, A: List[int], target: int) -> int:
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if (A[mid] < target):
                left = mid + 1
            elif (A[mid] > target):
                right = mid - 1
            else:
                # what if we found the number but its not rightmost?
                # we must continue to iterate right
                # case of out of bounds
                if (mid + 1 > len(A) - 1):
                    return mid
                # case of edge element: 0, 1, 4, 5, 5, 7, where 5, 7, we see 5 is on the edge
                elif (A[mid + 1] != target):
                    return mid
                left = mid + 1
        return -1