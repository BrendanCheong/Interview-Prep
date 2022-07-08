#link: https://leetcode.com/problems/maximum-subarray/submissions/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        O(n) solution
        O(1) space
        if the prefix/ the num before the end of the subarray decreases the max sum,
        drop that num from the sub array and reset the current value.
        This is a sliding window problem, remove negative prefixes as we compute total sum
        """
        max_num = nums[0]
        curr = 0 # initial value
        
        for ele in nums:
            if curr < 0: # if adding a ele gets a negative value, reset to 0 to get max sum
                curr = 0
            curr += ele # calculate the sum of this current subarray
            max_num = max(curr, max_num) # only take the max subarray
        # we only need to reset the curr value for a few reasons:
        # 1. if the current subarray is negative, we need to reset it to 0
        # 2. we don't need to reset if we encounter negative numbers
        return max_num
        