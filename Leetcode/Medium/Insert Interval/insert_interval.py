#link: https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals = sorted(intervals, key=lambda arr: arr[0])
        # assume already sorted by the start timings
        res = []
        START, END = 0, -1 # start and end of an array is 0, and -1
        
        for i, current_interval in enumerate(intervals):
            # edge cases:
            # new interval goes before all the intervals, no merging
            # new interval goes after all the intervals, no merging
            if (newInterval[END] < current_interval[START]):
                # if new interval end time is before the start time of the current interval,
                # it means we end earlier, so put it in the front(left side of array)
                res.append(newInterval)
                return res + intervals[i:] # new copy of remaining intervals
            elif (newInterval[START] > current_interval[END]):
                # interval start time is bigger than the end time of the current interval,
                # it means we start way later, so put to the end(right side of array)
                # don't return, there could be overlap with following intervals
                res.append(current_interval)
            else:
                # if there is overlap, we need to merge the intervals
                newInterval = [min(current_interval[START], newInterval[START]), max(current_interval[END], newInterval[END])]
                # its the min of the start time of the current interval and the new interval
        
        # if we reach here, means that first if condition never executed
        # as we are at the end of the array, so we need to append the new interval
        res.append(newInterval)

        return res

        