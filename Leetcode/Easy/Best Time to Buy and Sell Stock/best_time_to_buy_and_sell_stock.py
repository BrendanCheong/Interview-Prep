# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Solution is an O(N) solution with one iteration, followed by O(1) space.
        You could probably use dequeues to keep track of the sliding window, but that would be O(N) space.
        """
        # edge case
        if len(prices) < 2:
            return 0

        left, right = 0, 1
        MAX = -1

        # terminate when right is out-of-bounds of the array
        while right < len(prices):
            # need to immediately calculate since we start of from index 0 and 1
            if prices[left] < prices[right]:
                MAX = max(MAX, prices[right] - prices[left])
                right += 1
                # don't move the left since we found the best spot to buy at the moment
            elif prices[left] >= prices[right]:
                # if we find that we cannot make a profit
                #! NOTE: SHIFT THE LEFT POINTER all the way to the right!!!
                #! if we don't do this we wont update the left pointer to be the minimum price
                #! as the right pointer at this moment is the minimum price
                # then we cannot have both pointers at the same place, so move the right forward
                left = right
                right += 1
            
        return 0 if MAX == -1 else MAX


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
assert sol.maxProfit([7,1,5,3,6,4]) == 5
print(sol.maxProfit([7,6,4,3,1]))
assert sol.maxProfit([7,6,4,3,1]) == 0
print(sol.maxProfit([1,2,4,2,5,7,2,4,9,0,0,0,9]))
assert(sol.maxProfit([1,2,4,2,5,7,2,4,9,0,0,0,9])) == 9