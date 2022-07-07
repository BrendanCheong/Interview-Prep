# link: https://leetcode.com/problems/sort-colors/submissions/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        This is the QuickSort implementation or the Dutch-National Flag implementation
        This is a one pass O(N) solution that cleverly uses 3 buckets and swapping technique
        similar to quick sort.
        Note, this only works because there are 3 numbers to choose from.
        """
        zero, one, two = 0, 0, len(nums) - 1
        
        # we only focus on the middle as the pivot
        # terminate when one is exceeds two which means that the pointer on one has finished sorting
        # all the number one digits
        while one <= two:
            # one is the middle number, so we make sure that we want all number ones at the middle
            if nums[one] == 0:
                # if we find that one is 0, it means that one should go infront and swap with zero as its too far behind
                # so we swap with zero and one
                nums[one], nums[zero] = nums[zero], nums[one]
                one += 1
                zero += 1
                # increment both as we have successfully sorted a one and a zero
            elif nums[one] == 1:
                # since one is 1, its correct, so continue along the array
                # increment one, since we successfully sorted a one
                one += 1
            elif nums[one] == 2:
                # if we find that one is 2, one is too far ahead and must swap with two to go behind
                # so we swap with one and two
                # this time we decrease from two, as we have successfully sorted one of the twos
                nums[one] ,nums[two] = nums[two], nums[one]
                two -= 1

sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)
assert nums == [0,0,1,1,2,2]

edge = [1]
sol.sortColors(edge)
print(edge)
assert edge == [1]