#link: https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time: O(n log n), we must sort based on start value
        O(n) to merge all the intervals
        """
        START, END = 0, -1
        intervals = sorted(intervals, key=lambda int: int[START])
        # usually we can assume that its sorted according to start time, but in this case its not lol.
        res = []
        for i, curr_int in enumerate(intervals):
            prev = res[END] if res else None
            # edge cases:
            # new interval goes before all the intervals, no merging
            # new interval goes after all the intervals, no merging
            if (i == 0):
                # edge case where there is only 1 interval
                res.append(curr_int)
            elif (curr_int[START] <= prev[END]):
                # merge when there is an overlap
                merged_interval = [min(curr_int[START], prev[START]), max(curr_int[END], prev[END])]
                res.pop() and res.append(merged_interval)
                # we need to replace the previous interval with the merged interval
            else:
                # if there is no overlap, just append
                res.append(curr_int)
        return res
        
# test cases
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
print(s.merge([[1,4],[4,5]]))
assert s.merge([[1,4],[4,5]]) == [[1,5]]