# Merge Intervals

# Solution

When do we merge???

- We merge when the input[START] <= prev[END], means that there is an overlap!
- We do not merge when input[START] > prev[END]

How do we merge???
- We merge by taking finding [SMALLEST start among the 2, LARGEST END among the 2] as out interval
- **REPLACE** the prev interval with the **merged interval**. Remember to replace!!, not just add!

We can do an O(n) single pass from start to beginning to merge all the intervals and put in them in an empty result of list which we will return. Note: _**(not in-place)**_.

This also has O(n) memory or space.

However, since we cannot guarantee all intervals are sorted, the overall time complexity is O(n log n)

# Brute Force
Go through each and everyone of the intervals and see which one can merge for each interval in O(n^2) time