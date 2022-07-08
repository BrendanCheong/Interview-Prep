# Maximum Subarray

# Solution

We only need to reset the subarray if adding to the sub array causes the sum to drop to < 0 or negative number, as when we reach that, adding **any numbers would not make sense** as:
1. we can do better if the next num after the negative sum is positive
2. if the next num is negative theres no point in adding it

So we reset the subarray

If sliding window, we can just left `left_pointer = curr && right_pointer += 1` if we reset the subarray

# Brute Force
The brute force solution would be to create all possible subarrays in O(n^2) time and find the maximum using max(subarray, max_sum)
