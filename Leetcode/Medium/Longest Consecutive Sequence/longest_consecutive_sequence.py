from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Assumption: assume no repeated numbers.
        
        Brute force would be to sort in O(n log n) and find longest sequence
        Brute force would also to be check and find every number subsequence in O(2^n) or O(n^2) lookup
        
        The trick to this question is that we can know what number is the beginning of a sub-sequence
        by checking if it's left neighbour is in the list via a Set in O(1) lookup time.
        
        if there is no left number, its the beginning of the sub-sequence
        Then, we can start to find the next number after beginning, and again and again, unitl we cannot find anymore
        leading numbers
        
        use max to find the maximum length of the sequence
        
        
        NOTE: Another solution to this is to use the Good old Union-Find DS to quickly find and create groups
        """
        longest = 0
        num_set = set(nums)
        for num in nums:
            # check if its a start of a sub-sequence
            if not (num - 1) in num_set:
                # if no numbers behind it, its the start of a sub-sequence
                # so lets find how many numbers are in this sub-sequence!
                length = 0
                while (num + length) in num_set:
                    length += 1
                # now check to see if its the maximum longest sub-sequence
                longest = max(length, longest)
        return longest

# test cases
sol = Solution()
assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert sol.longestConsecutive([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
assert sol.longestConsecutive([-1, 0, 1]) == 2
assert sol.longestConsecutive([]) == 0