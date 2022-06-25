# Best Time to Buy and Sell Stock

## Brute Force
The brute force O(N^2) way would be check for each number what is the next biggest number in the array.
Then calculate the difference for each pair of numbers. Then find the maximum of that

## Sliding Window 
We must use a sliding window with 2 pointers.
first pointer is 0, second pointer is 1.

if the left or right pointer is out of bounds then `return 0`

our sliding window always calculates the profit which is `highest - lowest`
where the highest is `prices[right]` and the lowest is `prices[left]`
we always increment the right pointer, from `0 to len(prices)`
**The left pointer** changes when `left >= right` where it means that currently, the `right` pointer is the `lowest` element
and thus, the **left pointer must always be the lowest** so we do `left = right`

answer is going to be `MAX = max(MAX, profit)`

### Time & Space Complexity
O(N) time complexity as its only one iteration
O(1) space complexity as we only have 2 pointers in our sliding window
**if we used a dequeue** to store our sliding window we would have O(N) space.

## Edge case
If the array is less than 2 then its already `return 0` as we cannot sell stock.

