#link: https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        O(n log n) time, we always need to sort first
        """
        START, END = 0, -1 # start and end of an array is 0, and -1
        intervals = sorted(intervals, key=lambda int: int[START]) # sort by start time
        res, previous_int = 0, None
        for i, current_int in enumerate(intervals):
            if (i == 0):
                previous_int = current_int
            elif (current_int[START] >= previous_int[END]):
                # do not merge but just replace the previous interval with the current one
                # if equals, do not merge in this case
                previous_int = current_int
            else:
                # you can merge the intervals if there is overlap
                # NOTE: However, in this case, we want to only merge with the smallest end time interval
                # Because we want to REMOVE the overlapping interval
                res += 1
                previous_int = [max(current_int[START], previous_int[START]), min(current_int[END], previous_int[END])]
        return res

# test cases
s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
assert s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
assert s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
print(s.eraseOverlapIntervals([[1,2],[2,3]]))
assert s.eraseOverlapIntervals([[1,2],[2,3]]) == 0